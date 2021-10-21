import datetime
from typing import Union, Optional

from pydantic import BaseModel
from pydantic.validators import str_validator


def empty_to_none(v: str) -> Optional[str]:
    if v == '':
        return None
    return v


class EmptyStrToNone(str):
    @classmethod
    def __get_validators__(cls):
        yield str_validator
        yield empty_to_none
        

class AKA(BaseModel):
    title_id: Union[str, None, EmptyStrToNone]
    title: Union[str, None, EmptyStrToNone]
    region: Union[str, None, EmptyStrToNone]
    language: Union[str, None, EmptyStrToNone]
    types: Union[str, None, EmptyStrToNone]
    attributes: Union[str, None, EmptyStrToNone]
    is_original_title: bool


class Genre(BaseModel):
    genre: str


class Title(BaseModel):
    title_id: Union[str, None, EmptyStrToNone]
    type: Union[str, None, EmptyStrToNone]
    primary_title: Union[str, None, EmptyStrToNone]
    original_title: Union[str, None, EmptyStrToNone]
    is_adult: bool
    premiered: int
    ended: Union[int, None]
    runtime_minutes: int
    genres: list[Genre]
    

class Person(BaseModel):
    person_id: str
    name: Union[str, None, EmptyStrToNone]
    born: int
    died: int


class CrewMember(BaseModel):
    title_id: Union[str, None, EmptyStrToNone]
    person_id: Union[str, None, EmptyStrToNone]
    category: Union[str, None, EmptyStrToNone]
    job: Union[str, None, EmptyStrToNone]
    characters: Union[str, None, EmptyStrToNone]
    

class Rating(BaseModel):
    title_id: Union[str, None, EmptyStrToNone]
    rating: float
    votes: int
    
    
class Episode(BaseModel):
    episode_title_id: Union[str, None, EmptyStrToNone]
    show_title_id: Union[str, None, EmptyStrToNone]
    season_number: int
    episode_number: int
