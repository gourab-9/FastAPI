from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Hello welcome to my FastAPI!'}

# 01--- basic app
# 02--- pydantic demo
# 03--- models
# 04--- main
# 05--- model-val
# 06--- sync demo
# 07--- async demo
# 08--- async main