#!/usr/bin/python --2.7
# -*- coding: utf-8 -*-
import os
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf
from django.conf import settings
from PIL import Image

import re

from .models import Series, Season, Episode, Review, Like
from .forms import SeriesForm, SeasonForm, EpisodeForm, FilterForm,\
                   ReviewForm
from .choices import *

print(settings.MEDIA_ROOT)


# def user_is_author(request, review_id):
#         user = request.user
#         author_id = Review.objects.get(id=review_id).user_id
#         if user.id == author_id:
#             return True
#         else:
#             return False


def like_toggle_n_save(request, review_id):
    user = request.user
    try:
        likesrec_obj = Like.objects.get(review_id=review_id, user=user)
        author_id = Review.objects.get(id=review_id).user_id
        id=likesrec_obj.id
        is_liked = likesrec_obj.is_liked
        l = Like.objects.get(id=id)
        # print('user =', user.id, 'author =', author_id)
        if user.id != author_id:
            if is_liked == True:
                l.is_liked = False
                l.save()
            else:
                l.is_liked = True
                l.save()
    except Like.DoesNotExist:
        like_obj = Like(review_id=review_id, user=user, is_liked=True)
        like_obj.save()
    is_liked = get_object_or_404(Like, review_id=review_id, user=user).is_liked
    return  is_liked


def like_review(request, series_id, review_id):
    is_liked = like_toggle_n_save(request, review_id)
    print('after_save_is_liked =', is_liked)

    return HttpResponseRedirect('/vicat/'+series_id+'/reviews')


# def like_review(request, series_id):
#     rev_id = None
#     print('TEST')
#     if request.method == 'GET':
#         rev_id = request.GET['series_id']

#     likes = 0
#     if cat_id:
#         rev = Review.objects.get(id=int(rev_id))
#         if cat:
#             likes = cat.likes + 1
#             rev.likes =  likes
#             rev.save()
#     return HttpResponse(likes)



#


@staff_member_required
def delete_review(request, series_id, review_id):
    try:
        review_to_delete = Review.objects.get(pk=review_id).delete()
    except ObjectDoesNotExist:
        print( "Review doesn't exist.")
    return HttpResponseRedirect('/vicat/'+series_id+'/reviews')


@login_required
def edit_review(request, series_id, review_id):
    """ Update the review instance """
    series = get_object_or_404(Series, pk=series_id)
    if request.POST:
        review_edit_obj = Review.objects.get(series_id=series_id, id=review_id)
        form = SeasonForm(request.POST, instance=review_edit_obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id = review_id
            obj.series_id = series_id
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/vicat/'+series_id+'/reviews')

    else:
        text = get_object_or_404(Review, series_id=series_id,id=review_id).text
        data = {'series': series, 'user': request.user, 'text': text}
        form = ReviewForm(initial=data)

    context_dict = {}
    context_dict['is_editor'] = (request.user.is_active and
                                    request.user.is_staff)
    context_dict.update(csrf(request))
    context_dict['series_id'] = series_id
    context_dict['series'] = series
    context_dict['form'] = form
    context_dict['where'] = 'edit_review'
    return render(request, 'create_review.html', context_dict)

@login_required
def create_review(request, series_id):
    """ Create a new review instance """
    series = get_object_or_404(Series, pk=series_id)
    if request.POST:
        form = ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.series_id = series_id
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/vicat/'+series_id+'/reviews')

    else:
        data = {'series': series, 'user': request.user}
        form = ReviewForm(initial=data)

    context_dict = {}
    context_dict.update(csrf(request))
    context_dict['series_id'] = series_id
    context_dict['series'] = series
    context_dict['form'] = form
    context_dict['where'] = 'create_review'
    return render(request, 'create_review.html', context_dict)



def reviews(request, series_id):
    context_dict = {}
    print('is_liked - wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww - redirect')

    user = request.user
    review_list = Review.objects.filter(
                        series_id=series_id).all().order_by('-created')

    # access permission for voting (likes) =========
    for review in review_list:
        review_id=review.id

        author_id = Review.objects.get(id=review_id).user_id
        if user.id:
            if user.id == author_id:
                review.is_author = "is_author"
            else:
                review.is_author = "not_author"
        else:
            review.is_author = "anonimous"
        if user.username:
            try:
                likes_obj = Like.objects.get(review_id=review.id, user=user)
                if likes_obj.is_liked == True:
                    review.is_liked = True
                    review.is_liked_class = "is_liked"
                else:
                    review.is_liked = False
                    review.is_liked_class = "not_liked"
            except Like.DoesNotExist:
                review.is_liked = False
        else:
            review.is_liked = False
            review.is_liked_class = "not_liked"
            print('no username')
    # =========================

    review_count = review_list.count()
    series_title = get_object_or_404(Series, pk=series_id).title
    series = get_object_or_404(Series, pk=series_id)

    context_dict['user'] = user
    context_dict['is_editor'] = (request.user.is_active and
                                    request.user.is_staff)
    context_dict['series_title'] = series_title
    context_dict['series'] = series
    context_dict['review_count'] = review_count
    context_dict['review_list'] = review_list
    context_dict['likes_num'] = 101
    context_dict['where'] = 'reviews'

    return render(request, 'reviews.html', context_dict)


# new version  07022016===================================
@staff_member_required
def edit_episode(request, series_id, season_num, episode_id):
    """ Update the episode instance """
    episode_edit_obj = get_object_or_404(Episode, pk=episode_id)
    if request.POST:
        form = EpisodeForm(request.POST, instance=episode_edit_obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.series_id = series_id
            obj.season_num = season_num
            obj.save()

        return HttpResponseRedirect(
                                '/vicat/'+series_id+'/season/'+season_num)

    else:
        title = episode_edit_obj.title
        season = get_object_or_404(Season, series_id=series_id,
                                            season_num=season_num)
        series = get_object_or_404(Series, pk=series_id)
        data = {'series': series,
                'season': season,
                'season_num': season_num,
                'title': episode_edit_obj.title,
                'episode_num': episode_edit_obj.episode_num,
                'description': episode_edit_obj.description,
                'length': episode_edit_obj.length,
                'watch_count': episode_edit_obj.watch_count,
                }
        form = EpisodeForm(initial=data)
        form.fields['series'].widget.attrs['readonly'] = True
        form.fields['season'].widget.attrs['readonly'] = True
        form.fields['season_num'].widget.attrs['readonly'] = True
        form.fields['watch_count'].widget.attrs['readonly'] = True

    season_list = Season.objects.filter(
                        series_id=series_id).all().order_by('season_num')
    episode_list = Episode.objects.filter(
                        series_id=series_id).all().order_by('episode_num')
    context_dict = {}

    context_dict['cur_episode'] = episode_edit_obj
    context_dict.update(csrf(request))
    context_dict['form'] = form
    context_dict['series_id'] = series_id
    context_dict['season_list'] = season_list
    context_dict['season_num'] = season_num
    context_dict['episode_list'] = episode_list
    context_dict['episode_id'] = episode_id
    return render(request, 'edit_episode.html', context_dict)


# new version  07022016===================================
@staff_member_required
def create_episode(request, series_id, season_num):
    """ Create a new episode instance
        Prepare image file for saving
        Save new image name into db (name formed from the slug field)
    """
    if request.POST:
        form = EpisodeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.series_id = series_id
            obj.season_num = season_num
            obj.save()

        return HttpResponseRedirect(
                                '/vicat/'+series_id+'/season/'+season_num)

    else:
        season = get_object_or_404(Season, series_id=series_id,
                                            season_num=season_num)
        series = get_object_or_404(Series, pk=series_id)
        data = {'series': series, 'season': season, 'season_num': season_num}
        form = EpisodeForm(initial=data)
        form.fields['series'].widget.attrs['readonly'] = True
        form.fields['season'].widget.attrs['readonly'] = True
        form.fields['season_num'].widget.attrs['readonly'] = True

    season_list = Season.objects.filter(
                        series_id=series_id).all().order_by('season_num')
    episode_list = Episode.objects.filter(
                            series_id=series_id).all().order_by('episode_num')
    context_dict = {}
    context_dict.update(csrf(request))
    context_dict['form'] = form
    context_dict['series_id'] = series_id
    context_dict['season_list'] = season_list
    context_dict['season_num'] = season_num
    context_dict['episode_list'] = episode_list
    return render(request, 'create_episode.html', context_dict)
# =========================================


@staff_member_required
def edit_season(request, series_id, season_num):
    """ Update the season instance """
    if request.POST:
        season_edit_obj = Season.objects.get(series_id=series_id,
                                                season_num=season_num)
        form = SeasonForm(request.POST, instance=season_edit_obj)
        if form.is_valid():
            season_num = request.POST.get('season_num').encode('utf-8')
            # print("season_num =", season_num)
            form.save()

            return HttpResponseRedirect(
                                    '/vicat/'+series_id+'/season/'+season_num)

    else:
        series = get_object_or_404(Series, pk=series_id)
        season = Season.objects.get(series_id=series_id, season_num=season_num)
        # title = season.title
        data = {'series': series, 'season_num': season_num,
                'title': season.title}
        form = SeasonForm(initial=data)
        form.fields['series'].widget.attrs['readonly'] = True

    season_list = Season.objects.filter(
                        series_id=series_id).all().order_by('season_num')
    context_dict = {}
    context_dict.update(csrf(request))
    context_dict['form'] = form
    context_dict['series_id'] = series_id
    context_dict['season'] = season
    context_dict['season_list'] = season_list
    context_dict['season_num'] = season_num
    return render(request, 'edit_season.html', context_dict)


@staff_member_required
def create_season(request, series_id):
    """ Create a new season instance """
    if request.POST:
        print('series_id = ', series_id)
        form = SeasonForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.series_id = series_id
            obj.save()

            return HttpResponseRedirect('/vicat/'+series_id+'/seasons')

    else:
        series = get_object_or_404(Series, pk=series_id)
        data = {'series': series}
        form = SeasonForm(initial=data)
        form.fields['series'].widget.attrs['readonly'] = True

    season_list = Season.objects.filter(
                            series_id=series_id).all().order_by('season_num')
    context_dict = {}
    context_dict.update(csrf(request))
    context_dict['form'] = form
    context_dict['series_id'] = series_id
    context_dict['season_list'] = season_list
    return render(request, 'create_season.html', context_dict)

def series(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    istorrent = False
    context_dict = {}
    context_dict['is_editor'] = (request.user.is_active and
                                    request.user.is_staff)
    context_dict['title'] = series_title(request, series)

    episode_list_total = Episode.objects.filter(series_id=series_id).all()
    context_dict['episode_list_total'] = episode_list_total

    if series.torrent:
        istorrent = True
    print(istorrent)

    istorrent = True
    context_dict['istorrent'] = istorrent
    context_dict['review_count'] = Review.objects.filter(
                                series_id=series_id).all().count()
    context_dict['series'] = series
    context_dict['where'] = 'series'
    return render(request, "series.html", context_dict)


# new version 13022016=====================================
@staff_member_required
def edit_series(request, series_id):
    """ Update the series instance """
    context_dict = {}
    series = get_object_or_404(Series, pk=series_id)
    form = SeriesForm(request.POST or None,
                      request.FILES or None, instance=series)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/vicat/catalog/')

    return render(request, 'edit_series.html', {
                                'form': form,
                                'series': series,
                                'series_id': series_id})

# new version  13022016=====================================
@staff_member_required
def create_series(request):
    """ Create a new series instance
        Prepare image file for saving
        Save new image name into db (name formed from the slug attribute)
    """
    form = SeriesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/vicat/catalog/')

    return render(request, 'create_series.html', {'form': form})



def catalog(request):
    filterargs = {}
    fields = ('show_type', 'genre', 'country', 'language', 'subt_lan',
                    'active', 'istorrent', 'tosearch', 'viewed')
    if request.method == 'POST':
        form = FilterForm(request.POST)
        for field in fields:
            field_value = request.POST.get(field)
            if type(field_value) is not str:
                field_value = field_value.encode('utf-8')
            if (field_value != 'ALL'):
                if field_value == 'False':
                    field_value = False
                elif field_value == 'True':
                    field_value = True
                filterargs[field] = field_value

        found_entries = Series.objects.\
                            filter(**filterargs).order_by('created')

        is_editor = request.user.is_active and request.user.is_staff
        return render(request, 'catalog.html', {
                                'is_editor': is_editor,
                                'where': 'catalog',
                                'series_list': found_entries,
                                'form': form })
    else:
        form = FilterForm()

    context_dict = {}
    context_dict['form'] = form
    context_dict['is_editor'] = (request.user.is_active and
                                    request.user.is_staff)
    context_dict['series_list'] = Series.objects.all().order_by('title')
    context_dict['where'] = 'catalog'

    return render(request, 'catalog.html', context_dict)



def index(request):
    context_dict = {}
    context_dict['is_editor'] = (request.user.is_active and
                                    request.user.is_staff)
    series_list = Series.objects.all()
    context_dict['series_list'] = series_list
    return render(request, 'index.html', context_dict)

def seasons(request, series_id):
    context_dict = {}
    series = get_object_or_404(Series, pk=series_id)
    context_dict['is_editor'] = (request.user.is_active and
                                    request.user.is_staff)
    context_dict['title'] = series_title(request, series)
    context_dict['episode_list'] = Episode.objects.filter(
                                    series_id=series_id).all()
    context_dict['season_list'] = Season.objects.filter(
                            series_id=series_id).all().order_by('season_num')
    context_dict['avr_rate'] = 4.4
    context_dict['my_rate'] = 3.5
    context_dict['series'] = series
    context_dict['where'] = 'seasons'
    return render(request, "seasons.html", context_dict)

def inseason(request, series_id, season_num):
    context_dict = {}
    series = get_object_or_404(Series, pk=series_id)
    season_list = Season.objects.filter(
                            series_id=series_id).all().order_by('season_num')
    cur_season = Season.objects.get(series_id=series_id, season_num=season_num)

    context_dict['is_editor'] = (request.user.is_active and
                                    request.user.is_staff)
    context_dict['title'] = series_title(request, series)
    context_dict['season_num'] = season_num
    context_dict['episode_list'] = Episode.objects.filter(series_id=series_id,
                                                season_num=season_num).all()
    context_dict['season_list'] = season_list
    context_dict['cur_season'] = cur_season
    context_dict['avr_rate'] = 4.4
    context_dict['my_rate'] = 3.5
    context_dict['series'] = series
    context_dict['where'] = 'inseason'
    return render(request, "inseason.html", context_dict)

def episode(request, series_id, season_num, episode_id):
    context_dict = {}
    context_dict['avr_rate'] = 4.4
    context_dict['my_rate'] = 3.5
    istorrent = True

    series = get_object_or_404(Series, pk=series_id)
    season_list = Season.objects.filter(series_id=series_id).all()
    cur_season = Season.objects.get(series_id=series_id, season_num=season_num)
    cur_episode = get_object_or_404(Episode, id=episode_id)
    cur_episode_num = get_object_or_404(Episode, series_id=series_id,
                        season_num=season_num, pk=episode_id).season_num

    context_dict['is_editor'] = (request.user.is_active and
                                    request.user.is_staff)
    context_dict['title'] = series_title(request, series)
    context_dict['season_num'] = season_num
    context_dict['cur_episode'] = cur_episode
    context_dict['episode_list'] = Episode.objects.filter(series_id=series_id,
                        season_num=season_num).all().order_by('episode_num')
    context_dict['istorrent'] = istorrent
    context_dict['season_list'] = season_list
    context_dict['cur_season'] = cur_season
    context_dict['series'] = series
    context_dict['where'] = 'episode'
    return render(request, 'episode.html', context_dict)


def series_title(request, series):
    """ Extract full series title, including title and year """
    title = series.title
    if (series.year > 0):
        title += " (" + str(series.year) + ")"
    return title

def status_proc(request, series):
    """ Forms status fields for showing """
    istorrent = False
    if series.torrent:
        istorrent = True
    print(istorrent)
    result = (  'is' + str(series.viewed),
                'is' + str(series.active),
                'is' + str(istorrent),
                'is' + str(series.tosearch)
            )
    return (result)

#================ Delete Everything ======================

def delete_file(filename):
    """ Delete image file while deleted the associated database instance """
    try:
        os.remove(filename)
    except Exception as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        print 'Exception raised while deleting image file.'

def check_and_delete_files(series_to_delete):
    """ Checks and delete serial image file, episode image file """
    if series_to_delete.image_series.name:
        fname_series_to_delete = (settings.MEDIA_ROOT +
                                    series_to_delete.image_series.name)
        if os.path.isfile(fname_series_to_delete):
            print('fname_series_to_delete',fname_series_to_delete)
            delete_file(fname_series_to_delete)
        else:
            print('SERIES IMAGE FILE DOES NOT EXIST', fname_series_to_delete)
    else:
        print('NOTHING - NO series image in database to delete')
        # pass
    if series_to_delete.image_episode.name:
        fname_epis_to_delete = (settings.MEDIA_ROOT +
                                    series_to_delete.image_episode.name)
        if os.path.isfile(fname_epis_to_delete):
            print('fname_epis_to_delete',fname_epis_to_delete)
            delete_file(fname_epis_to_delete)
        else:
            print('EPISODE IMAGE FILE DOES NOT EXIST', fname_epis_to_delete)
    else:
        print('NOTHING - NO episode image in database to delete')
        # pass


@staff_member_required
def delete_series(request, series_id):
    """
        Than delete serial instance
    """
    try:        ## series instance deletion
        series_to_delete = Series.objects.get(id=series_id)
        check_and_delete_files(series_to_delete)  ## Image files deletion
        series_to_delete.delete()
    except ObjectDoesNotExist:
        print( "Series doesn't exist.")

    try:        ## Season instance deletion
        season_to_delete = Season.objects.get(series_id=series_id).delete()
        # pass
    except ObjectDoesNotExist:
        print( "Season doesn't exist.")

    try:        ## Episode instance deletion
        episode_to_delete = Episode.objects.get(series_id=series_id).delete()
        # pass
    except ObjectDoesNotExist:
        print( "Episode doesn't exist.")

    return HttpResponseRedirect(('/vicat/catalog/'))

@staff_member_required
def delete_season(request, series_id, season_num):
    try:
        season_to_delete = Season.objects.get(series_id=series_id,
                                        season_num=season_num).delete()
    except ObjectDoesNotExist:
        print( "Season doesn't exist.")
    try:
        episode_to_delete = Episode.objects.get(series_id=series_id,
                                        season_num=season_num).delete()
    except ObjectDoesNotExist:
        print( "Episode doesn't exist.")

    return HttpResponseRedirect(('/vicat/'+series_id+'/seasons'))

@staff_member_required
def delete_eppisode(request, series_id, season_num, episode_id):
    print('episode_id',episode_id)
    try:
        episode_to_delete = Episode.objects.get(pk=episode_id)
        episode_to_delete.delete()
    except ObjectDoesNotExist:
        print( "Episode doesn't exist.")
    return HttpResponseRedirect(('/vicat/'+series_id+'/season/'+season_num))

#================  ======================


#==================  search  ====================

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip())
                                for t in findterms(query_string)]

def get_query(query_string, search_fields):
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['title', 'director',])
        found_entries = Series.objects.filter(entry_query).order_by('-created')

    is_editor = request.user.is_active and request.user.is_staff
    form = FilterForm()
    return render(request, 'catalog.html', {
                            'is_editor': is_editor,
                            'query_string': query_string,
                            'series_list': found_entries,
                            'form': form })

#==================    ====================
