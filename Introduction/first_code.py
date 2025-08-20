from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, Welcome to FastAPI!'}

@app.get("/greet")
def greets(name:str):
    return {"message":f"Hello {name} Good Mornings"}

@app.get("/bmicalculator")
def bmicalculator(height: float, weight: float):
    """
    BMI Calculator using US units:
    - height in cms
    - weight in kg
    Formula: BMI = 703 * (weight / (height^2))
    """
    bmi = 703 * (weight / (height ** 2))
    return {"height": height, "weight": weight, "bmi": round(bmi, 2)}

# uvicorn first_code:app --reload
