import os

def populate():
    ser_qty = 5    ## Qty of series
    season_qty = 3  ## Qty of seasons in every serial
    ep_qty_in_season = 5 ## Qty of episodes in every season
    # Series population
    for ser_num in range(ser_qty):
        try:
            myseries = add_series(title = 'Series' + str(ser_num + 1),
                description = 'Some description for Series' + str(ser_num + 1),
                preview = 'preview_Series' + str(ser_num + 1),
                year = 2055,
                length = 30,
                season_qty = 10,
                episode_qty = 444,
                country = 'Japan',
                studio = 'Jap&Japa',
                language = 'Japan',
                # dub_lang = 'English',
                subt_lan = 'Russian',)
        except:
            pass

        # Season population
        for season_num in range(season_qty):
            try:
                myseason = add_season(
                    series = myseries,
                    title = 'Series' + str(ser_num + 1) + '-Season'
                                + str(season_num + 1),
                    season_num = season_num + 1,
                    )
            except:
                pass

            # Episode population
            for num in range(ep_qty_in_season):
                ep_num = (ep_qty_in_season * season_num) + num
                try:
                    add_episode(series = myseries,
                        season = myseason,
                        title = 'Title for Episode ' +
                                'ser' + str(ser_num + 1) +
                                's' + str(season_num + 1) +
                                'e' + str(ser_num*10 + ep_num + 1),
                        description = 'Some description for Episode ' +
                                'ser' + str(ser_num + 1) +
                                's' + str(season_num + 1) +
                                'e' + str(ser_num*10 + ep_num + 1),
                        preview = 'preview_' +
                                'ser' + str(ser_num + 1) +
                                's' + str(season_num + 1) +
                                'e' + str(ser_num*10 + ep_num + 1),
                        length = 30,
                        episode_num = ser_num*10 + ep_num + 1,
                        watch_count = 0,)
                except:
                    pass



def add_series(title, description, preview, year, length, season_qty,
                episode_qty, country, studio, language, dub_lang, subt_lan):
    ser = Series.objects.get_or_create(
        title = title,
        description = description,
        preview = preview,
        year = year,
        length = length,
        season_qty = season_qty,
        episode_qty = episode_qty,
        country = country,
        studio = studio,
        language = language,
        # dub_lang = dub_lang,
        subt_lan = subt_lan,)[0]
    return ser


def add_season(series, title, season_num):
    season = Season.objects.get_or_create(
        series = series,
        title = title,
        season_num = season_num,)[0]
    return season


def add_episode(series, season, title, description, preview, length,
                episode_num, watch_count):
    print(series.id, series.title)
    ep = Episode.objects.get_or_create(
        series = series,
        season = season,
        title = title,
        description = description,
        preview = preview,
        length = length,
        episode_num = episode_num,
        watch_count = watch_count,)[0]
    print('episode =============== ', ep.title)
    return ep

if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vipro.settings')

    import django
    django.setup()
    from vicat.models import Series, Episode, Season

    populate()