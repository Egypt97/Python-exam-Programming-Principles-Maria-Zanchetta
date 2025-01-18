from movie_library import MovieLibrary

if __name__ == "__main__":
    # Percorso assoluto del file JSON
    json_file_path = r"C:\Users\maria\OneDrive\Documenti\GitHub\Python-exam-Programming-Principles-Maria-Zanchetta\movies.json"
    
    # crea MovieLibrary
    try:
        library = MovieLibrary(json_file_path)
        print("Library initialized successfully!")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# versione finale        
  