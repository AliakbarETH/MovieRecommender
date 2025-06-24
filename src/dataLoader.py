from src.dataModels import MoviesDataModel, Genre
from typing import Dict 
import csv, os

path  = "data/movies.csv"

def moviesDataLoader(path : str) -> Dict [int, MoviesDataModel]:
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        movieDict = {}
        for row in reader:
            movieId = int(row["movieId"])
            title = row["title"]
            genres_str = row["genres"]
            if genres_str == "(no genres listed)":
                genres = []
            else:
                genres = []
                for g in genres_str.split("|"):
                    try:
                        genres.append(Genre(g))
                    except ValueError:
                        print(f"Warning: Invalid Genre '{g}' in movie_id {movieId}")

            moviesInstance = MoviesDataModel(
            movieId = movieId,
            title = title,
            genres = genres
            )
            movieDict[movieId] = moviesInstance

    return movieDict

#print(moviesDataLoader(path))

#print(os.path.exists(path)) 