#!/usr/bin/python --2.7
# -*- coding: utf-8 -*-
from django import forms

from .models import Series, Season, Episode, Review
from .choices import *


class SeriesForm(forms.ModelForm):

    description = forms.CharField(label="Описание",
                                    widget=forms.Textarea, required=False)
    title_trans = forms.CharField(label="Перевод названия",
                                    widget=forms.Textarea, required=False)
    note = forms.CharField(label="Заметки",
                                    widget=forms.Textarea, required=False)

    im_sourse_series = forms.ImageField(label="Источник фото", required=False,
                                    widget=forms.FileInput)
    im_sourse_episode = forms.ImageField(label="Источник фото", required=False,
                                    widget=forms.FileInput)

    class Meta:
        model = Series
        fields = ('title','description', 'year', 'length', 'studio', 'country',
                    'language', 'subt_lan',  'show_type', 'genre', 'director',
                    'actors', 'title_trans', 'preview_series', 'preview_episode',
                    'im_sourse_series', 'im_sourse_episode', 'viewed',
                    'active', 'istorrent', 'torrent', 'tosearch', 'note')



class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = '__all__'
        # fields = ('title', 'season_num')
        # exclude = ('episode_qty',)
        # readonly_fields = ['title','season_num']
        # form.fields['title'].widget.attrs['readonly'] = True

class EpisodeForm(forms.ModelForm):
    # series = forms.CharField(label="Название сериала", required=True)
    # season = forms.CharField(label="Название сезона", required=True)
    description = forms.CharField(label="Описание",
                                    widget=forms.Textarea, required=False)

    class Meta:
        model = Episode
        # fields = '__all__'
        fields = ('title', 'description', 'length', 'episode_num',
                    'watch_count', 'series', 'season_num', 'season')
        # fields = ('title', 'description', 'length', 'episode_num',
                    # 'watch_count', 'preview')


class ReviewForm(forms.ModelForm):
    text = forms.CharField(label="Добавьте ваш отзыв:",
                                    widget=forms.Textarea, required=True)
    class Meta:
        model = Review
        fields = '__all__'
        fields = ('text',)


class FilterForm(forms.Form):
    show_type = forms.ChoiceField(choices=FORM_TYPES, label="Тип",
                                widget=forms.Select())
    genre = forms.ChoiceField(choices=FORM_GENRES, label="Жанр",
                                widget=forms.Select())
    country = forms.ChoiceField(choices=FORM_COUNTRIES, label="Страна",
                                widget=forms.Select())
    language = forms.ChoiceField(choices=FORM_LANGUAGES, label="Язык",
                                widget=forms.Select())
    subt_lan = forms.ChoiceField(choices=FORM_SUBTITLES, label="Субтитры",
                                widget=forms.Select())

    active = forms.ChoiceField(choices=ACTIVE, label = 'Актив',
                                widget=forms.Select())
    istorrent = forms.ChoiceField(choices=ISTORRENT, label = 'Торрент',
                                widget=forms.Select())
    tosearch = forms.ChoiceField(choices=TOSEARCH, label = 'Искать',
                                widget=forms.Select())
    viewed = forms.ChoiceField(choices=VIEWED, label = 'Просмотрен',
                                widget=forms.Select())


    class Meta:
        fields = ('show_type', 'genre', 'country', 'language', 'subt_lan',
                    'active', 'istorrent', 'tosearch', 'viewed')










