from typing import List

from models import User, UserLogin, Tweet

from fastapi import FastAPI, status

app = FastAPI()

@app.get(path="/")
def home():
    """
        Welcome to app
    """
    return {"Twitter API": "Working!"}


@app.post(
    path="/signup", 
    response_model=User,
    status_code=status.HTTP_201_CREATED, 
    summary="Register a User", 
    tags=["Users"]
)
def signup():
    pass 


@app.post(
    path="/login", 
    response_model=User,
    status_code=status.HTTP_200_OK, 
    summary="Login a User", 
    tags=["Users"]
)
def login():
    pass 


@app.get(
    path="/users", 
    response_model=List[User],
    status_code=status.HTTP_200_OK, 
    summary="Show all Users", 
    tags=["Users"]
)
def show_all_users():
    pass 


@app.get(
    path="/users/{user_id}", 
    response_model=User,
    status_code=status.HTTP_200_OK, 
    summary="Show a User", 
    tags=["Users"]
)
def show_a_user():
    pass 


@app.delete(
    path="/users/{user_id}/delete", 
    status_code=status.HTTP_204_NO_CONTENT, 
    summary="Delete a User", 
    tags=["Users"]
)
def delete_a_user():
    pass 


@app.put(
    path="/users/{user_id}/update", 
    response_model=User,
    status_code=status.HTTP_202_ACCEPTED, 
    summary="Update a User", 
    tags=["Users"]
)
def update_a_user():
    pass 