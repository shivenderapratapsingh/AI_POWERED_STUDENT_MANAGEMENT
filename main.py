from typing import List, Optional
from fastapi import FastAPI, HTTPException
from models import Student,Feedback
from database import students
from nlp_utils import analyse_sentiment,smart_search
app = FastAPI(
    title="Studen Management Api",
    description="AI-Powered Restful API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message":"welcome to student management api"}

@app.post("/students",response_model=Student)
def create_student(student:Student):
    students.append(student)
    return student


@app.get("/students",response_model=List[Student])
def get_student():
    return students




@app.get("/students/{student_id}",response_model=Student)
def get_student(student_id:int):
    if student_id < 0 or student_id >=len(students):
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )
    return students[student_id]






@app.put("/students/{student_id}")
def update_student(student_id:int,name:str,updated_student:Student):
    print(name)
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    students[student_id]=updated_student

    return{
        "message":"student updated successfully",
        "data":updated_student
    }


@app.delete("/students/{student_id}")
def delete_student(student_id :int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    delete_student=students.pop(student_id)

    return{
        "message":"Student deleted successfully",
        "data":delete_student
    }
    
#filter students by course (Query parameter)
@app.get("/filter")#API end point -> /filter?course="string" or None
def filter_students(course: Optional[str]=None):
    if not course:
        return{"message":"Please provide course query parameter"}
    
    filtered=[
        s for s in students
        if s.course.lower()==course.lower()
    ]
    print("Start")
    for s in students:
        print(type(s))


    return {
        "count":len(filtered),
        "data":filtered
    }



@app.get("/search")
def search_student(name:str):
    result=[
        s for s in students if name.lower() in s.name.lower()
    ]

    if not result:
        raise HTTPException(
            status_code=404,
            detail="No student found with this name"
        )
    
    return{
        "Count":len(result),
        "Serached":result
    }




@app.post('/analyse-sentiment')
def sentiment_analysis(feed:Feedback):
    result=analyse_sentiment(feed.text)
    return{
        "text":feed.text,
        "analysis":result
    }


@app.post("/smart-search")
def  smart_searching(query:str):
    result=smart_search(students,query)
    if not result:
        raise HTTPException(
            status_code=404,
            detail="No student found with this name"
        )
    
    return{
        "Count":len(result),
        "Searched":result
    }


#staging area : like a prepration stage
#git add . ->it intialize staging area