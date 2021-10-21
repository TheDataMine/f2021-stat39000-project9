import sqlite3
from fastapi import HTTPException
from .database import queries, database_path
from .schemas import Title, Genre

def get_movie_with_id(title_id: str) -> Title:
    # Get the movie info from the database, and close
    # the database connection
    conn = sqlite3.connect(database_path)
    result = queries.get_movie_with_id(conn, title_id = title_id)
    conn.close()
    
    # If the result wasn't a movie, raise an exception
    if result[1] != 'movie':
        raise HTTPException(status_code=422, detail=f"Title with title_id '{title_id}' is not a movie, it is a {result[1]}.")
    
    # Split the genres by comma, and create a list of Genre objects
    listed_genres = result[8].split(',')
    genres = []
    for genre in listed_genres:
        genres.append(Genre(**{key: genre for _, key in enumerate(Genre.__fields__.keys())}))
    
    # Create a Title object, but manually set the genres entry in the Title object
    # to our list of Genres objects.
    movie = {key: result[i] for i, key in enumerate(Title.__fields__.keys())}
    movie['genres'] = genres
    movie = Title(**movie)

    return movie


def get_cast_for_title(title_id: str) -> list[CrewMember]:
    # Get the cast for the movie, and close the database connection
    conn = sqlite3.connect(database_path)
    results = queries.get_cast_for_title(conn, title_id = title_id)
    conn.close()

    # Create a list of dictionaries, where each dictionary is a cast member
    # INITIALIZE EMPTY LIST
    for member in results:
        crewmemberobject = CrewMember(**{key: member[i] for i, key in enumerate(CrewMember.__fields__.keys())})
        # APPEND crewmemberobject TO LIST

    return cast
