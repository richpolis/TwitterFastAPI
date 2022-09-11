from fastapi import FastAPI

app = FastAPI()

@app.get(path="/")
def home():
    """
        Welcome to app
    """
    return {"Twitter API": "Working!"}