from typing import Optional, List, Union
from datetime import datetime
from pydantic import BaseModel

class Movie(BaseModel):
    mid: int
    genre: str
    rate: Union[int, float] # rate는 int와 float 둘다 가능
    tag: Optional[str]=None # tag는 str이고, 기본값은 None
    date: Optional[datetime]=None #date는 datetime을 가지며 기본값은 None
    some_variable_list: List[int]=[] # 임의의 변수. 리스트값을 가지고 그 값들은 int여야함. 기본값은 []

tmp_data={
    'mid' : '1',
    'genre' : 'action',
    'rate' : 1.5,
    'tag' : None,
    'date' : '2025-01-05 13:11:11'
}
tmp_movie=Movie(**tmp_data)
print(tmp_movie)