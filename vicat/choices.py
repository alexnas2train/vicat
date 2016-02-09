#!/usr/bin/python --2.7
# -*- coding: utf-8 -*-




FIRST_LINE = ((u'ALL', u'любое'),)

TYPES = (
    (u'не указано', u'не указано'),
    (u'фильм', u'фильм'),
    (u'сериал', u'сериал'),
    (u'аниме', u'аниме'),
    (u'аниме-сериал', u'аниме-сериал'),
)

GENRES = (
    (u'не указано', u'не указано'),
    (u'комедия', u'комедия'),
    (u'трагедия', u'трагедия'),
    (u'мистика', u'мистика'),
    (u'семейный', u'семейный'),
)

COUNTRIES = (
    (u'не указано', u'не указано'),
    (u'Россия', u'Россия'),
    (u'США', u'США'),
    (u'Япония', u'Япония'),
    (u'Франция', u'Франция'),
    (u'Испания', u'Испания'),
    (u'Колумбия', u'Колумбия'),
    (u'Аргентина', u'Аргентина'),
    (u'Мексика', u'Мексика'),
)

LANGUAGES = (
    (u'не указано', u'не указано'),
    (u'RU', u'русский'),
    (u'EN', u'английский'),
    (u'ES', u'испанский'),
    (u'FR', u'французский'),
    (u'JP', u'японский'),
)

SUBTITLES = (
    (u'не указано', u'не указано'),
    (u'нет', u'отсутствуют'),
    (u'RU', u'русский'),
    (u'EN', u'английский'),
    (u'ES', u'испанский'),
    (u'FR', u'французский'),
    (u'JP', u'японский'),
)

FORM_TYPES = FIRST_LINE + TYPES
FORM_GENRES = FIRST_LINE + GENRES
FORM_COUNTRIES = FIRST_LINE + COUNTRIES
FORM_LANGUAGES = FIRST_LINE + LANGUAGES
FORM_SUBTITLES = FIRST_LINE + SUBTITLES


ACTIVE = (
    (u'ALL', u'любое'),
    (True, u'Да'),
    (False, u'Нет'),
)

ISTORRENT = (
    (u'ALL', u'любое'),
    (True, u'Да'),
    (False, u'Нет'),
)

TOSEARCH = (
    (u'ALL', u'любое'),
    (True, u'Да'),
    (False, u'Нет'),
)

VIEWED = (
    (u'ALL', u'любое'),
    (True, u'Да'),
    (False, u'Нет'),
)
