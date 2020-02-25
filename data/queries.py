from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_show_id():
    return data_manager.execute_select('SELECT id FROM shows;')


def get_all_episodes_for_show(show_id):
    return data_manager.execute_select("""
                                        SELECT shows.title, COUNT(episode_number) as episode_number FROM shows
                                        LEFT JOIN seasons s on shows.id = s.show_id
                                        LEFT JOIN episodes e on s.id = e.season_id
                                        WHERE show_id = %(show_id)s
                                        GROUP BY shows.title
    """, {'show_id': show_id})


def get_top_actors_id():
    return data_manager.execute_select("""
                                        SELECT show_characters.actor_id, a.name, COUNT(show_characters.character_name) as number_of_roles FROM show_characters
                                        LEFT JOIN actors a on show_characters.actor_id = a.id
                                        GROUP BY actor_id ,a.name
                                        ORDER BY number_of_roles desc
                                        LIMIT 10
    """)


def get_shows_by_min_season_numb(number):
    return data_manager.execute_select("""
                                        SELECT shows.title, COUNT(season_number) as number_of_seasons FROM shows
                                        LEFT JOIN seasons s on shows.id = s.show_id
                                        GROUP BY shows.title
                                        HAVING COUNT(season_number) >= %(number)s
    """, {"number": number})


def get_show_by_genre(my_genre):
    return data_manager.execute_select("""
                                        SELECT shows.title, shows.rating, genres.name as genre FROM shows
                                        INNER JOIN show_genres on shows.id = show_genres.show_id
                                        INNER JOIN genres on show_genres.genre_id = genres.id
                                        WHERE LOWER(genres.name) LIKE %(my_genre)s
                                        GROUP BY shows.title ,shows.rating,genres.name
                                        ORDER BY shows.rating DESC
                                        LIMIT 10
    """, {"my_genre": my_genre})


def get_actors_and_shows():
    return data_manager.execute_select("""
                                        SELECT DISTINCT actors.id, actors.name, ((actors.death-actors.birthday)/365) as age,COUNT(s.id) FROM actors
                                        INNER JOIN show_characters sc on actors.id = sc.actor_id
                                        RIGHT JOIN shows s on sc.show_id = s.id 
                                        WHERE actors.name IS NOT NULL 
                                        GROUP BY actors.id, actors.name,age,s.id                                      
                                        ORDER BY COUNT(s.id) DESC
    """)


def get_shows_by_runtime():
    return data_manager.execute_select("""
                                        SELECT  shows.id, shows.title ,(shows.runtime*count(episode_number)) AS total_runtime FROM shows 
                                        JOIN seasons s on shows.id = s.show_id
                                        JOIN episodes e on s.id = e.season_id
                                        GROUP BY shows.id,shows.title,shows.runtime
                                        ORDER BY total_runtime DESC 
                                        LIMIT 10
    """)


def get_actors_for_show_runtime(show_id):
    return data_manager.execute_select("""
                                        SELECT actors.name,s.id FROM actors
                                        JOIN show_characters sc on actors.id = sc.actor_id
                                        RIGHT JOIN shows s on sc.show_id = s.id
                                        WHERE s.id = %(show_id)s
                                        GROUP BY actors.name, s.id
                                        ORDER BY actors.name
    """, {"show_id": show_id})


def search_shows_by_title(search):
    return data_manager.execute_select("""
                                        SELECT shows.title,shows.rating,shows.year,shows.trailer FROM shows
                                        WHERE UPPER(shows.title) LIKE UPPER(%(search)s)
                                        GROUP BY shows.title, shows.rating, shows.year, shows.trailer
    """, {"search": "%"+search+"%"})


def get_actors_shows_avg(date):
    return data_manager.execute_select("""
                                    SELECT actors.name,COUNT(sc.character_name),ROUND((SUM(s.rating)/COUNT(s.rating)),2) AS avg_rating FROM actors
                                    RIGHT JOIN show_characters sc on actors.id = sc.actor_id
                                    RIGHT JOIN shows s on sc.show_id = s.id
                                    WHERE actors.name IS NOT NULL AND actors.birthday >= %(date)s
                                    GROUP BY actors.name
    """, {"date": date})
