from typing import List

from models import User, UserLogin, Tweet

from fastapi import FastAPI, status

app = FastAPI()

# Path Operations

## Users 

### Register User
@app.post(
    path="/signup", 
    response_model=User,
    status_code=status.HTTP_201_CREATED, 
    summary="Register a User", 
    tags=["Users"]
)
def signup():
    pass 

### Login User
@app.post(
    path="/login", 
    response_model=User,
    status_code=status.HTTP_200_OK, 
    summary="Login a User", 
    tags=["Users"]
)
def login():
    pass 


### Show all users
@app.get(
    path="/users", 
    response_model=List[User],
    status_code=status.HTTP_200_OK, 
    summary="Show all Users", 
    tags=["Users"]
)
def show_all_users():
    pass 

### Show a user 
@app.get(
    path="/users/{user_id}", 
    response_model=User,
    status_code=status.HTTP_200_OK, 
    summary="Show a User", 
    tags=["Users"]
)
def show_a_user():
    pass 

### Delete a user
@app.delete(
    path="/users/{user_id}/delete", 
    status_code=status.HTTP_204_NO_CONTENT, 
    summary="Delete a User", 
    tags=["Users"]
)
def delete_a_user():
    pass 

### Update a user
@app.put(
    path="/users/{user_id}/update", 
    response_model=User,
    status_code=status.HTTP_202_ACCEPTED, 
    summary="Update a User", 
    tags=["Users"]
)
def update_a_user():
    pass 


## Tweets

### Show all tweets
@app.get(
    path="/tweets", 
    response_model=List[Tweet], 
    status_code=status.HTTP_200_OK, 
    summary="Show all tweets", 
    tags=["Tweets"]
)
def show_all_tweets():
    return {"Twitter API": "Working!"}


### Register Tweet
@app.post(
    path="/tweets", 
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED, 
    summary="Register a Tweet", 
    tags=["Tweets"]
)
def create_tweet():
    pass 


### Show a tweet 
@app.get(
    path="/tweets/{tweet_id}", 
    response_model=Tweet,
    status_code=status.HTTP_200_OK, 
    summary="Show a Tweet", 
    tags=["Tweets"]
)
def show_a_tweet():
    pass 


### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete", 
    status_code=status.HTTP_204_NO_CONTENT, 
    summary="Delete a Tweet", 
    tags=["Tweets"]
)
def delete_a_tweet():
    pass 


### Update a tweet
@app.put(
    path="/tweets/{tweets_id}/update", 
    response_model=Tweet,
    status_code=status.HTTP_202_ACCEPTED, 
    summary="Update a Tweet", 
    tags=["Tweets"]
)
def update_a_tweet():
    pass 