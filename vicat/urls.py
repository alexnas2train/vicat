from django.conf.urls import url

# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)$', views.series, name='series'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/seasons$',
                                    views.seasons, name='seasons'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/season/(?P<season_num>[0-9]*)$',
                                    views.inseason, name='inseason'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/season/(?P<season_num>[0-9]*)/(?P<episode_id>[0-9]*)$',
                                    views.episode, name='episode'),
    url(r'^search/$', views.search, name='search'),
    url(r'^create_series/$', views.create_series, name='create_series'),
    url(r'^edit_series/(?P<series_id>[a-z,0-9,-]*)$',
                                    views.edit_series, name='edit_series'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/create_season$',
                                    views.create_season, name='create_season'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/edit_season/(?P<season_num>[0-9]*)$',
                                    views.edit_season, name='edit_season'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/season/(?P<season_num>[0-9]*)/create_episode$',
                                    views.create_episode, name='create_episode'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/season/(?P<season_num>[0-9]*)/edit_episode/(?P<episode_id>[0-9]*)$',
                                    views.edit_episode, name='edit_episode'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/season/(?P<season_num>[0-9]*)/delete_episode/(?P<episode_id>[0-9]*)$',
                                    views.delete_eppisode, name='delete_eppisode'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/season/(?P<season_num>[0-9]*)/delete_episode/(?P<episode_id>[0-9]*)$',
                                    views.delete_eppisode, name='delete_eppisode'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/delete_season/(?P<season_num>[0-9]*)$',
                                    views.delete_season, name='delete_season'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/delete_series$',
                                    views.delete_series, name='delete_series'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/reviews$',
                                    views.reviews, name='reviews'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/create_review$',
                                    views.create_review, name='create_review'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/edit_review/(?P<review_id>[0-9]*)$',
                                    views.edit_review, name='edit_review'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/delete_review/(?P<review_id>[0-9]*)$',
                                    views.delete_review, name='delete_review'),
    url(r'^(?P<series_id>[a-z,0-9,-]*)/like_review/(?P<review_id>[0-9]*)$',
                                    views.like_review, name='like_review'),


]



