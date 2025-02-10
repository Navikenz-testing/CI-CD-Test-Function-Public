from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/test")
def read_test():
    return {"message": "This is a test endpoint"}

lambda_handler = Mangum(app)
