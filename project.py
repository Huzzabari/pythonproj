from PyMovieDb import IMDB
import json
import plotly.express as px


def main():  # main file
    movies, count = return_movies()  # get data
    print_movies(movies, count)  # print this data as a list in the console
    plot_movies_by_year(movies)  # graph this information


def return_movies():  # return list function (might make it a list of dictionaries later if i can)
    imdb = IMDB()
    valid_genres = [
        "action",
        "adventure",
        "animation",
        "biography",
        "comedy",
        "crime",
        "documentary",
        "drama",
        "family",
        "fantasy",
        "film-noir",
        "history",
        "horror",
        "music",
        "musical",
        "mystery",
        "romance",
        "sci-fi",
        "short",
        "sport",
        "thriller",
        "war",
        "western",
    ]

    choose = choose_genre(valid_genres)
    if choose is None:
        return [], 0
    else:
        try:
            res = imdb.popular_movies(
                genre=choose, start_id=1, sort_by=None
            )  # gives a response of that genre
        except Exception as e:
            print(f"Error: {e}")

        data = json.loads(res)  # translate the json file into a dict for python to read
        count = int(data["result_count"])  # get the results count
        temp_list = []  # make a list
        for i in range(count):  # appending the names of the movies to the list
            movie_data = {
                "name": data["results"][i]["name"],
                "year": data["results"][i]["year"],
            }
            temp_list.append(movie_data)  # add to list
        unique_movies = []  # make a list of movies that are unique and not dublicates
        seen_names = (
            set()
        )  # this is a list that stores movies and checks if their are duplicates with the set method

        for (
            movie
        ) in (
            temp_list
        ):  # foor loop where if the movie name key pair is not in the set list(seen_names) it appends the movie dict to the unique movies list and adds the movie name to the seen names list
            if movie["name"] not in seen_names:
                unique_movies.append(movie)
                seen_names.add(movie["name"])

        return unique_movies, count
        # return movie_list, count  # returning this data to the main program


def choose_genre(valid_genres):
    choose = (
        input("What genre of movie are you looking for? ").lower().strip()
    )  # asks the user which genre they are looking for
    if (
        choose in valid_genres
    ):  # if choice is in genres then return it.  Otherwise return nothing and tell the user.
        return choose
    else:
        print("Genre not found.  Please try again.")
        return None


def print_movies(movies, count):  # prints the movie title and year with key value pairs
    for movie in movies:
        print(f"Movie Title: {movie['name']}, Year: {movie['year']}")
    print(f"from {count} results!")  # prints total results searched


def plot_movies_by_year(movies):
    # Create a Plotly scatter plot
    fig = px.scatter(  # figure makes a scatter plot of the movies list of dicts.
        movies,
        x="year",
        title="Top Movies by Year",
        labels={
            "year": "Year",
            "name": "Movie Title",
        },  # label of year and movie title.  I'm organizing this information by year.
        hover_data=["name"],  # display movie name when hovering over dot
    )

    # Show the chart
    fig.show()


if __name__ == "__main__":
    main()
