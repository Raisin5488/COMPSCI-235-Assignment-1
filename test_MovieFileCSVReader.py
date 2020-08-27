import pytest
from Actor import Actor
from Director import Director
from Genre import Genre
from Movie import Movie
from MovieFileCSVReader import MovieFileCSVReader

@pytest.fixture
def movieFileCSVReader():
    return MovieFileCSVReader('Data1000Movies.csv')

def test_given():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()

    assert len(file_reader.dataset_of_movies) == 1000
    assert len(file_reader.dataset_of_actors) == 1985
    assert len(file_reader.dataset_of_directors) == 644
    assert len(file_reader.dataset_of_genres) == 20

def test_other():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()

    all_directors_sorted = sorted(file_reader.dataset_of_directors)
    assert all_directors_sorted[0:3] == [Director("Aamir Khan"), Director("Abdellatif Kechiche"), Director("Adam Leon")]

def test_average_runtime():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert file_reader.calculate_average_runtime() == 113

def test_average_rating():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert (file_reader.calculate_average_rating()) == 6.7

def test_average_votes():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert (file_reader.calculate_average_votes()) == 169808

def test_average_revenue_millions():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert (file_reader.calculate_average_revenue_millions()) == 82.96

def test_average_metascore():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert (file_reader.calculate_average_metascore()) == 59

def test_movie_descriptopn():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert file_reader.dataset_of_movies[0].description == "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe."

def test_movie_runtime():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert file_reader.dataset_of_movies[0].runtime_minutes == 121


def test_movie_rating():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert file_reader.dataset_of_movies[0].rating == 8.1

def test_movie_votes():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert file_reader.dataset_of_movies[0].votes == 757074

def test_movie_revenue():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert file_reader.dataset_of_movies[0].revenue_millions == 333.13

def test_movie_metascore():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert file_reader.dataset_of_movies[0].metascore == 76

def test_movie_revenue_NA():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert file_reader.dataset_of_movies[7].revenue_millions == 0

def test_movie_metascore_NA():
    filename = 'Data1000Movies.csv'
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()
    assert file_reader.dataset_of_movies[25].metascore == 0

