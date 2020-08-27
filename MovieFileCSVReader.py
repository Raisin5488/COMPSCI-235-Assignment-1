import csv
from Actor import Actor
from Director import Director
from Genre import Genre
from Movie import Movie

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

        self.__total_runtime_minutes = 0
        self.__runtime_minutes_number_of_movies = 0
        self.__total_rating = 0
        self.__rating_number_of_movies = 0
        self.__total_votes = 0
        self.__votes_number_of_movies = 0
        self.__total_revenue_millions = 0
        self.__revenue_millions_number_of_movies = 0
        self.__total_metascore = 0
        self.__metascore_number_of_movies = 0

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            index = 0
            for row in movie_file_reader:
                movie = Movie(row["Title"], int(row["Year"]))
                movie.description = row["Description"]
                movie.runtime_minutes = int(row["Runtime (Minutes)"])
                self.__total_runtime_minutes += int(row["Runtime (Minutes)"])
                self.__runtime_minutes_number_of_movies += 1
                if row["Rating"] != "N/A":
                    movie.rating = float(row['Rating'])
                    self.__total_rating += float(row['Rating'])
                    self.__rating_number_of_movies += 1
                if row["Votes"] != "N/A":
                    movie.votes = int(row["Votes"])
                    self.__total_votes += int(row["Votes"])
                    self.__votes_number_of_movies += 1
                if row["Revenue (Millions)"] != "N/A":
                    movie.revenue_millions = float(row["Revenue (Millions)"])
                    self.__total_revenue_millions += float(row["Revenue (Millions)"])
                    self.__revenue_millions_number_of_movies += 1
                if row["Metascore"] != "N/A":
                    movie.metascore = int(row["Metascore"])
                    self.__total_metascore += int(row["Metascore"])
                    self.__metascore_number_of_movies += 1

                self.__dataset_of_movies.append(movie)
                self.__dataset_of_directors.add(Director(row["Director"]))
                for actor in row["Actors"].split(","):
                    self.__dataset_of_actors.add(Actor(actor.strip()))
                for genre in row["Genre"].split(","):
                    self.__dataset_of_genres.add(Genre(genre.strip()))
                index += 1

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    def calculate_average_runtime(self):
        return round(self.__total_runtime_minutes / self.__runtime_minutes_number_of_movies)

    def calculate_average_rating(self):
        return round(self.__total_rating / self.__rating_number_of_movies, 1)

    def calculate_average_votes(self):
        return round(self.__total_votes / self.__votes_number_of_movies)

    def calculate_average_revenue_millions(self):
        return round(self.__total_revenue_millions / self.__revenue_millions_number_of_movies, 2)

    def calculate_average_metascore(self):
        return round(self.__total_metascore / self.__metascore_number_of_movies)

filename = 'Data1000Movies.csv'
file_reader = MovieFileCSVReader(filename)
file_reader.read_csv_file()
print(file_reader.dataset_of_movies[0].description)
