from flask import Flask, render_template,request
from data import queries
from datetime import datetime
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    actors = queries.get_top_actors_id()
    return render_template("index.html", actors=actors, shows=shows)


@app.route('/tv-show/<int:show_id>')
def show_list(show_id):
    all_episodes = queries.get_all_episodes_for_show(show_id)
    return render_template('tv_show.html', all_episodes=all_episodes, is_long=None)


@app.route('/search', methods=["GET", "POST"])
def search_min_max():
    my_numb = request.form.get("min_numb")
    if my_numb is not int:
        error = "Sorry give us a number"
    shows = queries.get_shows_by_min_season_numb(my_numb)
    return render_template("search_field.html", error=error, shows=shows)


@app.route('/ratings',methods=["GET", "POST"])
def getting_top_shows():
    my_genre = request.form.get("my_genre")
    show_by_genre = queries.get_show_by_genre(my_genre)
    return render_template("show_by_genre.html",shows=show_by_genre)


@app.route('/most-active')
def show_most_active_actors():
    active_actors = queries.get_actors_and_shows()
    return render_template('most_active_actors.html',active_actors=active_actors)


@app.route('/shows-runtime')
def show_shows_by_runtime():
    show_by_runtime = queries.get_shows_by_runtime()
    actors = []
    for shows in show_by_runtime:
        actors.append(queries.get_actors_for_show_runtime(shows["id"]))
    return render_template('shows_by_runtime.html', show_by_runtime=show_by_runtime, actors=actors)


@app.route('/search-shows', methods=["GET", "POST"])
def search_shows():
    search_word = request.form.get("search_word")
    right_shows = queries.search_shows_by_title(str(search_word))
    return render_template('search-show.html', right_shows=right_shows)


@app.route('/avg-actor', methods=["GET","POST"])
def show_avg_actor():
    date = request.form.get("user_date")
    right_date = str(date)+"-1-1"
    actors = queries.get_actors_shows_avg(right_date)
    return render_template("actor_avg_shows.html", actors=actors)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
