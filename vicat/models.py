# -*- coding: utf-8 -*-
#!/usr/bin/python --2.7
from __future__ import unicode_literals
import os

import string
import random
import datetime

from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.conf import settings
from django import forms
from .choices import *



class OverwriteStorage(FileSystemStorage):
    ''' Overwrite existing filename if already exist '''
    print('settings.MEDIA_ROOT',settings.MEDIA_ROOT)
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

def get_upload_path_ser(instance, filename, **kwargs):
    ''' File will be uploaded to MEDIA_ROOT/+images/+fff+slug+extension '''
    ext = filename.split('.')[-1]
    return '{0}/{1}{2}.{3}'.format('images', 'fff', instance.slug, ext)

def get_upload_path_epis(instance, filename):
    ''' File will be uploaded to MEDIA_ROOT/+images/+sss+slug+extension '''
    name, ext = filename.split('.')
    return '{0}/{1}{2}.{3}'.format('images', 'sss', instance.slug, ext)

class Series(models.Model):
    id = models.UUIDField(primary_key = True,default=uuid.uuid4,editable=False)
    slug = models.SlugField(max_length=30, primary_key=False, blank=True)
    title = models.CharField(u'название**', max_length=128, unique=True)
    description = models.CharField(u'описание', max_length=1024, blank=True,
                                    default='Описание не оформлено')
    image_series = models.ImageField (u'данные о фото_сер', blank=True,
                                    upload_to=get_upload_path_ser,
                                    storage=OverwriteStorage())
    image_episode = models.ImageField (u'данные о фото_эп', blank=True,
                                    upload_to=get_upload_path_epis,
                                    storage=OverwriteStorage())
    preview_series = models.CharField(u'имя фото сериала', blank=True, max_length=128,
                                   null=True)
    preview_episode = models.CharField(u'имя фото эпизода', blank=True, max_length=128,
                                   null=True)
    year = models.IntegerField(u'год выпуска', default=0, blank=False)
    length = models.IntegerField(u'длительность', default=0)
    season_qty = models.IntegerField(u'кол-во сезонов',
                                    default=0, editable=False)
    episode_qty = models.IntegerField(u'кол-во эпизодов',
                                    default=0, editable=False)
    country = models.CharField(u'страна', max_length=50,
                                    choices=COUNTRIES, default='')
    studio = models.CharField(u'студия', blank=True, max_length=128)
    language = models.CharField(u'язык', max_length=50,
                                    choices=LANGUAGES, default='')
    subt_lan = models.CharField(u'субтитры', max_length=50,
                                    choices=SUBTITLES, default='')
    director = models.CharField(u'режисер', blank=True, max_length=64)
    actors = models.CharField(u'актеры', blank=True, max_length=256)
    title_trans = models.CharField(u'перевод названия',
                                    blank=True, max_length=256)
    genre = models.CharField(u'жанр', max_length=50,
                                    choices=GENRES, default='')
    show_type = models.CharField(u'тип', max_length=50,
                                    choices=TYPES, default='')
    viewed = models.BooleanField(u'просмотрено', default=False)
    active = models.BooleanField(u'актив', default=False)
    istorrent = models.BooleanField(u'торрент', blank=True, default=False)
    torrent = models.CharField(u'торрент-адрес', blank=True, max_length=512,
                                    default='')
    tosearch = models.BooleanField(u'искать',default=False)
    created = models.DateTimeField(u'дата создания', auto_now_add=True,
                                    auto_now=False, null=True, blank=True)
    updated = models.DateTimeField(u'дата последнего изменения',
                                    auto_now_add = False, auto_now=True)
    note = models.CharField(u'заметки', max_length=1024, blank=True,
                                    default='заметки администратора')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Сериал"
        verbose_name_plural = u"Сериалы"

    def save(self, *args, **kwargs):
        date = datetime.datetime.today()
        if not self.slug:
            self.slug = '%i%i%i-%i%i%i-%s' % (
                        date.year, date.month, date.day, date.hour,
                        date.minute, date.second, slugify(self.title)[:10],
                    )
        super(Series, self).save(*args, **kwargs)


class Season(models.Model):
    title = models.CharField(u'название сезона', max_length=128)
    season_num = models.IntegerField(u'номер сезона', blank=False)
    episode_qty = models.IntegerField(u'кол-во эпизодов', blank=False,
                                        default=0, editable=False)
    series = models.ForeignKey(Series)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Сезон"
        verbose_name_plural = u"Сезоны"
        unique_together = (('season_num', 'series'),('title', 'series'),)


class Episode(models.Model):
    title = models.CharField(u'название эпизода', max_length=128)
    description = models.CharField(u'описание', max_length=1024,
                                    default='Описание не оформлено')
    length = models.IntegerField(u'длительность', default=0)
    season_num = models.IntegerField(u'номер сезона', default=0)
    episode_num = models.IntegerField(u'номер эпизода', default=0)
    watch_count = models.IntegerField(u'кол-во просмотров', default=0)
    created = models.DateTimeField(u'дата создания', auto_now_add=True,
                                    auto_now=False, null=True, blank=True)
    updated = models.DateTimeField(u'дата последнего изменения',
                                    auto_now_add = False, auto_now=True)
    series = models.ForeignKey(Series)
    season = models.ForeignKey(Season)


    def __unicode__(self):
        return u'Эпизод %s' % (self.title)

    class Meta:
        verbose_name = u"Эпизод"
        verbose_name_plural = u"Эпизоды"
        unique_together = (('episode_num', 'series'), ('title', 'series'),)
        # unique_together = (('episode_num', 'season_num', 'series'), ('title', 'series'),)

    def save(self, *args, **kwargs):
        self.season_num = self.season.season_num
        super(Episode, self).save(*args, **kwargs)

        try:
            cur_season = Season.objects.get(series_id=self.series_id,
                                    season_num=self.season.season_num)
            cur_season.episode_qty = Episode.objects.filter(
                                    series_id=self.series_id,
                                    season_num=self.season.season_num).count()
            cur_season.save()
        except Season.DoesNotExist:
            print('Exception of Error for Season model')
            pass

        try:
            cur_series = Series.objects.get(id=self.series_id)
            cur_series.episode_qty = Episode.objects.filter(
                                    series_id=self.series_id).count()
            cur_series.season_qty = Season.objects.filter(
                                    series_id=self.series_id).count()
            print('season_qty = ', cur_series.season_qty)
            cur_series.save()
        except Series.DoesNotExist:
            print('Exception of Error for Series model')
            pass


class Review(models.Model):
    text = models.CharField(u'текст', max_length=256)
    created = models.DateTimeField(u'дата создания', auto_now_add=True,
                                    auto_now=False, null=True, blank=True)
    updated = models.DateTimeField(u'дата последнего изменения',
                                    auto_now_add = False, auto_now=True)
    series = models.ForeignKey(Series)
    user = models.ForeignKey(User)
    likes = models.IntegerField(u'кол-во лайков', default=0)

    def __unicode__(self):
        return u'Отзыв %s' % (self.text)

    class Meta:
        verbose_name = u"Отзыв"
        verbose_name_plural = u"Отзывы"

    def calculate_likes(self):
        return Like.objects.filter(review=self, is_liked=True).count()

    likes_count = property(calculate_likes)

    def check_likes(self, cur_user):
        if Like.objects.filter(review=self, user=cur_user).is_liked == True:
            return True
        else: return False

    likes_check = property(check_likes)



class Like(models.Model):
    is_liked = models.BooleanField(u'лайк',default=False)
    review = models.ForeignKey(Review)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'Лайк %s' % (self.review)

    class Meta:
        verbose_name = u"Лайк"
        verbose_name_plural = u"Лайки"

    def check_likes(self):
        if Like.objects.filter(review=self, user=cur_user).is_liked == True:
            return True
        else: return False

    likes_check = property(check_likes)


