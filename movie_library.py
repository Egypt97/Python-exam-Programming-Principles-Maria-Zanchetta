import json
from typing import List, Optional


class MovieNotFoundError(Exception):
    """Eccezione personalizzata per gli errori se non si trova un film."""
    pass


class MovieLibrary:
    def __init__(self, json_file: str):
        """
        Inizializzo e inserisco il percorso del file JSON.
        Il percorso assoluto è nel file esterno.
        Movie viene deserializzato
        Solleva l'eccezione FileNotFoundError se il file non viene trovato.
        Esercizio 17
        """
        self.json_file = json_file
        try:
            with open(self.json_file, 'r') as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File non trovato: {self.json_file}")
        except json.JSONDecodeError:
            self.movies = []

    def __update_json_file(self):
        """
        Metodo privato.
        Aggiorna il file JSON per riflettere le modifiche nella collezione.
        """
        with open(self.json_file, 'w') as file:
            json.dump(self.movies, file, indent=4)

    def get_movies(self) -> List[dict]:
        """
        Restituisce l'intera collezione di film.
        Esercizio 1
        """
        return self.movies

    def add_movie(self, title: str, director: str, year: int, genres: List[str]):
        """
        Aggiunge un nuovo film alla collezione e aggiorna il file JSON.
        Esercizio 2
        """
        if not title.strip():
            raise ValueError("Title field cannot be empty.")
        if not director.strip():
            raise ValueError("The director's field cannot be empty.")
        if not isinstance(year, int) or year < 1900:
            raise ValueError("The year must be an integer equal to or higher than 1900.")
        if not isinstance(genres, list) or not all(isinstance(genre, str) for genre in genres):
            raise ValueError("Genres must be a list of strings.")

        new_movie = {
            "title": title.strip(),
            "director": director.strip(),
            "year": year,
            "genres": [genre.strip() for genre in genres],
        }
        self.movies.append(new_movie)
        self.__update_json_file()

    def remove_movie(self, title: str) -> dict:
        """
        Rimuove un film dalla collezione per titolo e aggiorna il file JSON.
        Esercizio 3 ed eccezione di esercizio 18
        """
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                self.movies.remove(movie)
                self.__update_json_file()
                return movie
        raise MovieNotFoundError(f"Movie '{title}' was not found.")

    def update_movie(
        self,
        title: str,
        director: Optional[str] = None,
        year: Optional[int] = None,
        genres: Optional[List[str]] = None,
    ) -> dict:
        """
        Modifica i dati di un film e aggiorna il file JSON.
        Esercizio 4 ed eccezione di esercizio 18
        """
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                if director:
                    movie["director"] = director.strip()
                if year:
                    if not isinstance(year, int) or year < 1900:
                        raise ValueError("The year must be an integer greater or equal to 1900.")
                    movie["year"] = year
                if genres:
                    if not isinstance(genres, list) or not all(isinstance(genre, str) for genre in genres):
                        raise ValueError("Genres must be a list of strings.")
                    movie["genres"] = [genre.strip() for genre in genres]
                self.__update_json_file()
                return movie
        raise MovieNotFoundError(f"Movie '{title}' was not found.")

    def get_movie_titles(self) -> List[str]:
        """
        Restituisce una lista con tutti i titoli dei film nella collezione.
        Esercizio 5
        """
        return [movie["title"] for movie in self.movies]

    def count_movies(self) -> int:
        """
        Restituisce il numero totale di tutti i film nella collezione.
        Esercizio 6
        """
        return len(self.movies)

    def get_movie_by_title(self, title: str) -> Optional[dict]:
        """
        Restituisce un film in base al titolo indicato.
        Esercizio 7
        """
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                return movie
        return None

    def get_movies_by_title_substring(self, substring: str) -> List[dict]:
        """
        Trova film in base a una sottostringa presente nel titolo.
        Esercizio 8
        """
        return [movie for movie in self.movies if substring.lower() in movie["title"].lower()]

    def get_movies_by_year(self, year: int) -> List[dict]:
        """
        Restituisce i film dell'anno indicato.
        Esercizio 9
        """
        return [movie for movie in self.movies if movie["year"] == year]

    def count_movies_by_director(self, director: str) -> int:
        """
        Restituisce il numero di film diretti da un regista specifico.
        Esercizio 10
        """
        return sum(1 for movie in self.movies if movie["director"].lower() == director.lower())

    def get_movies_by_genre(self, genre: str) -> List[dict]:
        """
        Restituisce una lista di film che appartengono al genere specificato.
        Esercizio 11
        """
        return [
            movie for movie in self.movies
            if genre.lower() in (g.lower() for g in movie["genres"])
        ]

    def get_oldest_movie_title(self) -> Optional[str]:
        """
        Restituisce il titolo del film più vecchio nella collezione.
        Esercizio 12
        """
        if not self.movies:
            return None
        return min(self.movies, key=lambda x: x["year"])["title"]

    def get_average_release_year(self) -> float:
        """
        Calcola la media aritmetica degli anni di pubblicazione dei film.
        Esercizio 13
        """
        if not self.movies:
            return 0.0
        return sum(movie["year"] for movie in self.movies) / len(self.movies)

    def get_longest_title(self) -> Optional[str]:
        """
        Restituisce il titolo più lungo nella collezione di film.
        Esercizio 14
        """
        if not self.movies:
            return None
        return max(self.movies, key=lambda x: len(x["title"]))["title"]

    def get_titles_between_years(self, start_year: int, end_year: int) -> List[str]:
        """
        Trova i titoli di film usciti tra due anni inclusivi.
        Esercizio 15
        """
        return [
            movie["title"] for movie in self.movies
            if start_year <= movie["year"] <= end_year
        ]

    def get_most_common_year(self) -> Optional[int]:
        """
        Restituisce l'anno più comune tra i film della collezione.
        Esercizio 16
        """
        if not self.movies:
            return None
        year_counts = {}
        for movie in self.movies:
            year = movie["year"]
            year_counts[year] = year_counts.get(year, 0) + 1
        return max(year_counts, key=year_counts.get)

# versione finale