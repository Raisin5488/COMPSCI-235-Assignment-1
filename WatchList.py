from Movie import Movie

class WatchList:
    def __init__(self):
        self.__movie_list = []

    @property
    def movie_list(self):
        return self.__movie_list

    def add_movie (self, movie):
        if movie not in self.movie_list:
            self.movie_list.append(movie)
    
    def remove_movie (self, movie):
        if movie in self.movie_list:
            self.movie_list.remove(movie)

    def select_movie_to_watch(self, index):
        if index >= self.size() or index < 0:
            return None
        else:
            return self.movie_list[index]

    def size(self):
        return len(self.movie_list)

    def first_movie_in_watchlist(self):
        if self.size() == 0:
            return None
        else:
            return self.movie_list[0]

    def __iter__(self):
        self.number = -1
        return self

    def __next__(self):
        self.number += 1
        return self.movie_list[self.number]
