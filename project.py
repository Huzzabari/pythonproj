from PyMovieDb import IMDB
import json


def main():  # main file
    (
        movies,
        count,
    ) = return_list()  # so far returns the movies and the count of the total results
    for movie in movies:  # prints each movie title and the the result number
        print(movie)
    print(f"from {count} results!")


def return_list():  # return list function (might make it a list of dictionaries later if i can)
    imdb = IMDB()
    choose = input(
        "What genre of movie are you looking for? "
    )  # asks the user which genre they are looking for
    res = imdb.popular_movies(
        genre=choose, start_id=1, sort_by=None
    )  # gives a response of that genre
    data = json.loads(res)  # translate the json file into a dict for python to read
    count = int(data["result_count"])  # get the results count
    temp_list = []  # make a list
    for i in range(count):  # appending the names of the movies to the list
        temp_list.append(data["results"][i]["name"])
    # print(res)
    movie_list = set(temp_list)  # removing duplicates
    return movie_list, count  # returning this data to the main program



if __name__ == "__main__":
    main()
