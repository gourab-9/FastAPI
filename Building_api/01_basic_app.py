from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Hello welcome to my FastAPI!'}

