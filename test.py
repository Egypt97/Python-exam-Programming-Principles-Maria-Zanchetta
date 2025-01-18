"""
Test di tutti i metodi della classe precedente
Code in English, commenti in italiano
"""

from movie_library import MovieLibrary


def display_menu():
    print("\n--- Movie Library Menu ---")
    print("1. View all movies")  # test esercizio 1
    print("2. Add a new movie")  # test esercizio 2
    print("3. Remove a movie")  # test esercizio 3
    print("4. Update a movie")  # test esercizio 4
    print("5. Get all movie titles")  # test esercizio 5
    print("6. Count total number of movies")  # test esercizio 6
    print("7. Search for a movie by title")  # test esercizio 7
    print("8. Search for movies by title substring")  # test esercizio 8
    print("9. Get movies by year")  # test esercizio 9
    print("10. View movies by genre")  # test esercizio 11
    print("11. Count movies by director")  # test esercizio 10
    print("12. Find the oldest movie")  # test esercizio 12
    print("13. Get the average release year")  # test esercizio 13
    print("14. Get the longest movie title")  # test esercizio 14
    print("15. View movies released between two years")  # test esercizio 15
    print("16. Get the most common release year")  # test esercizio 16
    print("17. Exit")


def view_all_movies(library):
    # tutti i film della collezione
    print("\n--- All Movies ---")
    for movie in library.get_movies():
        print(movie)


def add_movie(library):
    # aggiunge un nuovo film alla libreria
    print("\n--- Add a New Movie ---")
    title = input("Title: ")
    director = input("Director: ")
    try:
        year = int(input("Release year: "))
    except ValueError:
        print("Invalid year. Please enter a valid number.")
        return
    genres = input("Genres (comma-separated): ").split(",")
    library.add_movie(title, director, year, [g.strip() for g in genres])
    print(f"The movie '{title}' was added successfully!")


def remove_movie(library):
    # rimuove un film a scelta
    print("\n--- Remove a Movie ---")
    title = input("Enter the title of the movie to remove: ")
    try:
        removed_movie = library.remove_movie(title)
        print(f"Removed movie: {removed_movie}")
    except Exception as e:
        print(f"Error: {e}")


def update_movie(library):
    # aggiorna la libreria riguardo ad un film
    print("\n--- Update a Movie ---")
    title = input("Enter the title of the movie to update: ")
    director = input("New director (leave empty to keep unchanged): ")
    year = input("New year (leave empty to keep unchanged): ")
    genres = input("New genres (comma-separated, leave empty to keep unchanged): ")
    try:
        director = director if director else None
        year = int(year) if year else None
        genres = [g.strip() for g in genres.split(",")] if genres else None
        updated_movie = library.update_movie(title, director=director, year=year, genres=genres)
        print(f"Updated movie: {updated_movie}")
    except Exception as e:
        print(f"Error: {e}")


def get_movie_titles(library):
    # mostra tutti i titoli dei film
    print("\n--- Get All Movie Titles ---")
    titles = library.get_movie_titles()
    for title in titles:
        print(title)


def count_movies(library):
    # mostra il numero dei film presenti nella collezione
    print("\n--- Count Total Number of Movies ---")
    count = library.count_movies()
    print(f"There are {count} movies in the collection.")


def search_movie_by_title(library):
    # ricerca film in base al titolo
    print("\n--- Search for a Movie by Title ---")
    title = input("Enter the title of the movie to search: ")
    movie = library.get_movie_by_title(title)
    if movie:
        print("Found movie:", movie)
    else:
        print("Movie not found.")


def search_movies_by_title_substring(library):
    # cerca i film in base alla substring
    print("\n--- Search for Movies by Title Substring ---")
    substring = input("Enter the substring: ")
    movies = library.get_movies_by_title_substring(substring)
    for movie in movies:
        print(movie)


def get_movies_by_year(library):
    # mostra i film usciti in un determinato anno
    print("\n--- Get Movies by Year ---")
    try:
        year = int(input("Enter the release year: "))
        movies = library.get_movies_by_year(year)
        if movies:
            for movie in movies:
                print(movie)
        else:
            print(f"No movies found from the year {year}.")
    except ValueError:
        print("Invalid year. Please enter a valid number.")


def get_movies_by_genre(library):
    # indica i film che appartengono ad un determinato genere
    print("\n--- View Movies by Genre ---")
    genre = input("Enter the genre: ")
    movies_by_genre = library.get_movies_by_genre(genre)
    if movies_by_genre:
        print(f"Movies in the genre '{genre}':")
        for movie in movies_by_genre:
            print(movie)
    else:
        print(f"No movies found in the genre '{genre}'.")


def count_movies_by_director(library):
    # conta i film di un determinato regista
    print("\n--- Count Movies by Director ---")
    director = input("Enter the director's name: ")
    count = library.count_movies_by_director(director)
    print(f"Number of movies directed by '{director}': {count}")


def find_oldest_movie(library):
    # trova il film più vecchio
    print("\n--- Find the Oldest Movie ---")
    oldest = library.get_oldest_movie_title()
    if oldest:
        print(f"The oldest movie is: {oldest}")
    else:
        print("The library is empty.")


def get_average_release_year(library):
    # calcola la media degli anni di uscita dei film presenti
    print("\n--- Get the Average Release Year ---")
    average_year = library.get_average_release_year()
    print(f"The average release year is: {average_year:.2f}")


def get_longest_title(library):
    # trova il titolo del film più lungo
    print("\n--- Get the Longest Movie Title ---")
    longest_title = library.get_longest_title()
    if longest_title:
        print(f"The longest title is: {longest_title}")
    else:
        print("No longest title found.")


def get_titles_between_years(library):
    # indica i titoli dei film usciti in un determinato lasso di tempo
    print("\n--- View Movies Released Between Two Years ---")
    try:
        start_year = int(input("Start year: "))
        end_year = int(input("End year: "))
        titles = library.get_titles_between_years(start_year, end_year)
        print(f"Movies released between {start_year} and {end_year}: {titles}")
    except ValueError:
        print("Invalid input. Please enter valid years.")


def get_most_common_year(library):
    # trova l'anno più frequente nell'uscita dei film
    print("\n--- Get the Most Common Release Year ---")
    most_common_year = library.get_most_common_year()
    if most_common_year:
        print(f"The most common release year is: {most_common_year}")
    else:
        print("The library is empty.")


def main():
    library = MovieLibrary("movies.json")

    while True:
        display_menu()
        choice = input("Choose an option (1-17): ")

        if choice == "1":
            view_all_movies(library)
        elif choice == "2":
            add_movie(library)
        elif choice == "3":
            remove_movie(library)
        elif choice == "4":
            update_movie(library)
        elif choice == "5":
            get_movie_titles(library)
        elif choice == "6":
            count_movies(library)
        elif choice == "7":
            search_movie_by_title(library)
        elif choice == "8":
            search_movies_by_title_substring(library)
        elif choice == "9":
            get_movies_by_year(library)
        elif choice == "10":
            get_movies_by_genre(library)
        elif choice == "11":
            count_movies_by_director(library)
        elif choice == "12":
            find_oldest_movie(library)
        elif choice == "13":
            get_average_release_year(library)
        elif choice == "14":
            get_longest_title(library)
        elif choice == "15":
            get_titles_between_years(library)
        elif choice == "16":
            get_most_common_year(library)
        elif choice == "17":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# versione finale