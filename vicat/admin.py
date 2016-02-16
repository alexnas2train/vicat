#!/usr/bin/python --2.7
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Series, Season, Episode, Review, Like

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'country')


admin.site.register(Series)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Review)
admin.site.register(Like)
