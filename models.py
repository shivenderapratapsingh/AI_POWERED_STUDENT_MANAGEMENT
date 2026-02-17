from pydantic import BaseModel,EmailStr
from typing import Optional
#pydantic used for automatic validation of input request data
#if you enter worng data type than it automatically do type casting beacus eof base model
class Student(BaseModel):
    name:str
    age:int
    course:str
    email:Optional[EmailStr]=None



class Feedback(BaseModel):
    text:str

#base model help in do json serilization

# class Professor(BaseModel):
#     pid:int
#     name:str
#     experience:int
#     subject:str
#     email:str