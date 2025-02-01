from typing import Optional, List, Union
from datetime import datetime
from pydantic import BaseModel, Field

class Movie(BaseModel):
    mid: int
    genre: str
    rate: Union[int, float] # rate는 int와 float 둘다 가능
    tag: Optional[str]=None # tag는 str이고, 기본값은 None
    date: Optional[datetime]=None #date는 datetime을 가지며 기본값은 None
    some_variable_list: List[int]=[] # 임의의 변수. 리스트값을 가지고 그 값들은 int여야함. 기본값은 []


class User(BaseModel):
    '''
    gt : 설정된 값보다 큰
    ge : 설정된 값보다 크거나 같은
    lt : 설정된 값보다 작은
    le : 설정된 값보다 작거나 같은
    '''
    uid : int
    name : str = Field(min_length=2, max_length=7)
    age : int = Field(gt=1, le=130)

tmp_data={
    'mid' : '1',
    'genre' : 'action',
    'rate' : 1.5,
    'tag' : None,
    'date' : '2025-01-05 13:11:11'
}

tmp_user_data={
    'uid' : '100',
    'name' : 'minkyu',
    'age' : '30',
}
tmp_movie=Movie(**tmp_data)
tmp_user_data=User(**tmp_user_data)
print(tmp_movie)
print(tmp_user_data)