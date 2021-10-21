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
    is_original_title: Union[bool, None]


class Genre(BaseModel):
    genre: Union[str, None, EmptyStrToNone]


class Title(BaseModel):
    title_id: Union[str, None, EmptyStrToNone]
    type: Union[str, None, EmptyStrToNone]
    primary_title: Union[str, None, EmptyStrToNone]
    original_title: Union[str, None, EmptyStrToNone]
    is_adult: Union[bool, None]
    premiered: Union[int, None]
    ended: Union[int, None]
    runtime_minutes: Union[int, None]
    genres: list[Genre]
    

class Person(BaseModel):
    person_id: Union[str, None, EmptyStrToNone]
    name: Union[str, None, EmptyStrToNone]
    born: Union[int, None]
    died: Union[int, None]


class CrewMember(BaseModel):
    title_id: Union[str, None, EmptyStrToNone]
    person_id: Union[str, None, EmptyStrToNone]
    category: Union[str, None, EmptyStrToNone]
    job: Union[str, None, EmptyStrToNone]
    characters: Union[str, None, EmptyStrToNone]
    

class Rating(BaseModel):
    title_id: Union[str, None, EmptyStrToNone]
    rating: Union[float, None]
    votes: Union[int, None]
    
    
class Episode(BaseModel):
    episode_title_id: Union[str, None, EmptyStrToNone]
    show_title_id: Union[str, None, EmptyStrToNone]
    season_number: Union[int, None]
    episode_number: Union[int, None]
