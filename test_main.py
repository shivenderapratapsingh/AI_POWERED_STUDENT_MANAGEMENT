import pytest
from fastapi.testclient import TestClient
from main import app
#a fixture function which we create to test again and again it is a reusable 
#to be reused again and again for testing
@pytest.fixture
def client():
    return TestClient(app) #we are passing object of Fastapi

#dependency injection :-we prepared it outside and used to inside some function just like client we defined outside then it injected in test case
@pytest.fixture
def post_sample_data():
    return [{"name":"billu","age":22,"email":"billu@gamil.com","course":"Chemistry"},{"name":"shivaay","age":33,"email":"shiva@gmail.com","course":"english"}]
@pytest.fixture
def post_checkupdate_data():
    return []

def test_home(client): #they will 
    response=client.get("/")
    assert response.status_code==200
    assert response.json()=={"message":"welcome to student management api"}

def test_add_student(client, post_sample_data):
    respose=client.post("/students",json=post_sample_data[0])
    assert respose.status_code==200
    assert respose.json()["name"]=="billu"
    assert respose.json()["age"]==22
    assert respose.json()["email"]=="billu@gamil.com"
    assert respose.json()["course"]=="Chemistry"

def test_data_validate(client, post_sample_data): #not a local paramete it is a fixture name
    response = client.get("/students/0")
    assert response.status_code == 200
    assert response.json() == post_sample_data[0]



def test_get_students(client):
    response = client.get("/students")
    assert response.status_code==200
    assert isinstance(response.json(),list)
    assert len(response.json())>=1

def test_update_students(client, post_sample_data):
    respose=client.put("/students/0",json=post_sample_data[1])
    assert respose.json()["message"]=="student updated successfully"
    assert respose.json()["data"]==post_sample_data[1]



def test_filter_data(client,post_sample_data):
    response=client.get("/filter",params={"course":"english"})
    assert response.status_code == 200
    assert response.json()["data"][0]==post_sample_data[1]
     
def test_delete_student(client, post_sample_data):
    response=client.delete("/students/0")
    assert response.json()["message"]=="Student deleted successfully"
    assert response.json()["data"]==post_sample_data[1]


#pytest writing test cases assertion 
#Testclient is used to perform testing we sent request using testclient we send request to fast api
#when we run pytest -v it scan the complete project files and go to that function which start with test_ so there is no need to call on our own
#assert it checks the conditon is valid or not