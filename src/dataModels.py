from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum


# defining data model for movies.csv file

class Genre(Enum):
    Action = "Action" 
    Adventure = "Adventure" 
    Animation = "Animation"
    Children = "Children"
    Comedy = "Comedy"
    Crime = "Crime"
    Documentary = "Documentary"
    Drama = "Drama"
    Fantasy = "Fantasy"
    FilmNoir = "Film-Noir"
    Horror = "Horror"
    Musical = "Musical"
    Mystery = "Mystery"
    Romance = "Romance"
    SciFi = "Sci-Fi"
    Thriller = "Thriller"
    War = "War"
    Western = "Western"
    IMAX = "IMAX"

class MoviesDataModel(BaseModel):
    movieId: int
    title : str
    genres : List[Genre]
    
# defining data model for user_rating_history.csv file

class UserRatingHistoryModel(BaseModel):
    userId : int 
    movieId: int  
    rating : float 
    tstamp : datetime

# defining data model for belief_data.csv file

class BeliefDataModel(BaseModel):
    userId: int
    movieId: int
    isSeen: int  
    watchDate: Optional[datetime]
    userElicitRating: Optional[float]
    userPredictRating: Optional[float]
    userCertainty: Optional[float]
    tstamp: datetime 
    movie_idx: int
    source: int
    systemPredictRating: float