from src.dataModels import MoviesDataModel, Genre, UserRatingHistoryModel
from typing import Dict 
import csv
from datetime import datetime

moviesPath  = "data/movies.csv"
userRatingPath = "data/user_rating_history.csv"

def moviesDataLoader(moviesPath : str) -> Dict [int, MoviesDataModel]:
    movieDict = {}
    with open(moviesPath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
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

def userRatingHistoryLoader(userRatingPath : str) -> Dict [int,UserRatingHistoryModel]:
    UserRatingHistoryDict = {}
    with open(userRatingPath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            userId = int(row["userId"])
            movieId = int(row["movieId"])
            tstamp = datetime.strptime(row["tstamp"], "%Y-%m-%d %H:%M:%S")
            if row["rating"] == "NA":
                continue
            else:
                rating = float(row["rating"])
            UserRatingInstance = UserRatingHistoryModel(
                    userId = userId,
                    movieId = movieId, 
                    rating = rating, 
                    tstamp = tstamp
            )
            UserRatingHistoryDict[userId] = UserRatingInstance
    return UserRatingHistoryDict

print(userRatingHistoryLoader(userRatingPath))