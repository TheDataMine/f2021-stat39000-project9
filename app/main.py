from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from app.schemas import AKA, Title, Person, Crew, Rating, Episode
from app.imdb import get_movie_with_id


app = FastAPI()
templates = Jinja2Templates(directory='templates/')


@app.get("/")
async def root():
    """
    Returns a simple message, "Hello World!"

    Returns:
        dict: The response JSON.
    """
    return {"message": "Hello World"}


@app.get(
    "/movies/{title_id}", 
    response_model=Title, 
    summary="Get a movie with title_id.",
    response_description="A movie."
)
async def get_movies(title_id: str):
    movie = get_movie_with_id(title_id)
    return movie
