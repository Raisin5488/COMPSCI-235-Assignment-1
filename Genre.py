class Genre:

    def __init__(self, genre_name : str):
        if genre_name  == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name (self) -> str:
        return self.__genre_name
    
    @genre_name.setter
    def genre_name (self, genre_name : str) -> str:
        if genre_name  == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if self.genre_name == other.genre_name:
            return True
        return False

    def __lt__(self, other):
        return self.genre_name < other.genre_name 

    def __hash__(self):
        return hash(self.genre_name)

