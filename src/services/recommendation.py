from src.dataModels import MoviesDataModel, Genre
from src.dataLoader import moviesDataLoader
from src.services.openai_helper import extract_genres_from_text
from typing import Dict, List
moviesPath = "data/movies.csv"
movies = moviesDataLoader(moviesPath)

# def get_user_selected_genre() -> List[Genre]:
#     user_input = input("Enter your preferred genres separated by commas: ")
#     genres = []
#     for g in user_input.split(","):
#         g_clean = g.strip()
#         try:
#             genre_enum = Genre(g_clean)
#             genres.append(genre_enum)
#         except ValueError:
#             print(f"⚠️ Warning: '{g_clean}' is not a valid genre and will be skipped.")
#     return genres


def get_user_selected_genre() -> List[Genre]:
    mode = input("Type 'ai' for GPT-assisted input or 'manual' for manual genre entry: ").strip().lower()

    genres = []

    if mode == "ai":
        user_input = input("Tell me what kind of movies you like: ")
        genre_names = extract_genres_from_text(user_input)

        for g in genre_names:
            try:
                genres.append(Genre(g))
            except ValueError:
                print(f"⚠️ Warning: '{g}' is not a valid genre and will be skipped.")
    else:
        user_input = input("Enter your preferred genres separated by commas: ")
        for g in user_input.split(","):
            g_clean = g.strip()
            try:
                genres.append(Genre(g_clean))
            except ValueError:
                print(f"⚠️ Warning: '{g_clean}' is not a valid genre and will be skipped.")
    
    return genres

def get_movies_by_genre(movies: Dict[int, MoviesDataModel], selected_genres: List[Genre]) -> List[MoviesDataModel]:
    filtered = []
    for movie in movies.values():
        if any(g in movie.genres for g in selected_genres):
            filtered.append(movie)
    return filtered

def display_movies(movies: List[MoviesDataModel], limit: int = 10):
    print(f"\nTop {min(len(movies), limit)} movies based on your genres:\n")
    for movie in sorted(movies, key=lambda m: m.title)[:limit]:
        genre_list = ", ".join([g.value for g in movie.genres])
        print(f"{movie.title} ({genre_list})")

# CLI run
if __name__ == "__main__":
    selected_genres = get_user_selected_genre()
    filtered_movies = get_movies_by_genre(movies, selected_genres)
    display_movies(filtered_movies)
