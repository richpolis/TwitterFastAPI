import json
from typing import List

from models import User, UserRegister, Tweet

from fastapi import FastAPI, status, Body

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
def signup(user: UserRegister = Body(...)):
    """
    Signup a user

    This path operation register a user in the app 

    Parameters:
        - Request body parameter
            - user: UserRegister
    
    Returns a json with the basic user information:
        - user_ui: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open('users.json', 'r+', encoding='UTF-8') as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict['user_ui'] = str(user_dict['user_ui'])
        user_dict['birth_date'] = str(user_dict['birth_date'])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user
        

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
    """
    Show all users

    This path operation show all users in the app

    Parameters:
        - 
    
    Returns a json with the basic user information, with the following keys:
        - user_ui: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open('users.json', 'r', encoding='UTF-8') as f:
        results = json.loads(f.read())
        return results

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
    """
    Show all tweets

    This path operation show all tweets in the app

    Parameters:
        - 
    
    Returns a json with the basic user information, with the following keys:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: datetime
        - by: User
    """
    with open('tweets.json', 'r', encoding='UTF-8') as f:
        results = json.loads(f.read())
        return results


### Register Tweet
@app.post(
    path="/tweets", 
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED, 
    summary="Register a Tweet", 
    tags=["Tweets"]
)
def create_tweet(tweet: Tweet = Body(...)):
    """
    Post a tweet

    This path operation post a tweet in the app 

    Parameters:
        - Request body parameter
            - tweet: Tweet
    
    Returns a json with the basic user information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open('tweets.json', 'r+', encoding='UTF-8') as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict['tweet_id'] = str(tweet_dict['tweet_id'])
        tweet_dict['created_at'] = str(tweet_dict['created_at'])
        if 'updated_at' in tweet_dict:
            tweet_dict['updated_at'] = str(tweet_dict['updated_at'])
        tweet_dict['by']['user_ui'] = str(tweet_dict['by']['user_ui'])
        tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date']) 
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet


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