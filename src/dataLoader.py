from src.dataModels import MoviesDataModel, Genre, UserRatingHistoryModel, BeliefDataModel
from typing import Dict 
import csv
from datetime import datetime



def moviesDataLoader(path : str) -> Dict [int, MoviesDataModel]:
    movieDict = {}
    with open(path, "r", encoding="utf-8") as f:
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
                    g_clean = g.strip()
                    if not g_clean:
                        continue
                    try:
                        genres.append(Genre(g_clean))
                    except ValueError:
                        print(f"Warning: Invalid Genre '{g}' in movie_id {movieId}")

            moviesInstance = MoviesDataModel(
            movieId = movieId,
            title = title,
            genres = genres
            )
            movieDict[movieId] = moviesInstance

    return movieDict

def userRatingHistoryLoader(path : str) -> Dict [int,UserRatingHistoryModel]:
    UserRatingHistoryDict = {}
    with open(path, "r", encoding="utf-8") as f:
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

def BeliefDataLoader(path : str) -> Dict [int, BeliefDataModel]:
    BeliefDataDict = {}
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            userId = int(row["userId"])
            movieId = int(row["movieId"])
            isSeen = int(row["isSeen"])  
            watchDate = (
                datetime.strptime(row["watchDate"], "%Y-%m-%d %H:%M:%S")
                if row["watchDate"].strip() != ""
                else None
            )            
            userElicitRating = (
                float(row["userElicitRating"])
                if row["userElicitRating"].strip() not in ["", "NA"]
                else None 
            )
            userPredictRating = (
                float(row["userPredictRating"])
                if row["userPredictRating"].strip() not in ["", "NA"]
                else None
            )
            userCertainty = (
                float(row["userCertainty"])
                if row["userCertainty"].strip() not in ["", "NA"]
                else None
            )
            tstamp = datetime.strptime(row["tstamp"], "%Y-%m-%d %H:%M:%S" )
            movie_idx = int(row["movie_idx"])
            source = int(row["source"])
            systemPredictRating = float(row["systemPredictRating"])
            beliefDataInstance = BeliefDataModel (
                    userId = userId,
                    movieId = movieId,
                    isSeen = isSeen, 
                    watchDate = watchDate,
                    userElicitRating = userElicitRating,
                    userPredictRating = userPredictRating,
                    userCertainty = userCertainty,
                    tstamp = tstamp,
                    movie_idx = movie_idx,
                    source = source,
                    systemPredictRating = systemPredictRating
            )
            BeliefDataDict[userId] = beliefDataInstance

    return BeliefDataDict


