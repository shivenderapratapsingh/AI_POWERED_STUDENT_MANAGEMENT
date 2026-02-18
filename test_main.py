import pytest
from fastapi.testclient import TestClient
from main import app
#a fixture function which we create to test again and again it is a reusable 
#to be reused again and again for testing
@pytest.fixture
def client():
    # create a Testcli
    return TestClient(app) #we are passing object of Fastapi

#dependency injection :-we prepared it outside and used to inside some function just like client we defined outside then it injected in test case
@pytest.fixture
def post_sample_data():
    return {"name":"shiv","age":22,"email":"shivaay@gamil.com","course":"AIML"}

def test_home(client): #they will 
    response=client.get("/")
    assert response.status_code==200
    assert response.json()=={"message":"welcome to student management api"}

def test_data(client, post_sample_data):
    # First create student
    client.post("/students", json=post_sample_data)

    # Then fetch student
    response = client.get("/students/0")

    assert response.status_code == 200
    assert response.json() == post_sample_data

#pytest writing test cases assertion 
#Testclient is used to perform testing we sent request using testclient we send request to fast api
#when we run pytest -v it scan the complete project files and go to that function which start with test_ so there is no need to call on our own
#assert it checks the conditon is valid or not