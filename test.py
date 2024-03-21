# from fastapi import FastAPI, Form
# from pydantic import BaseModel

# app = FastAPI()

# class MyForm(BaseModel):
#     name: str
#     email: str

# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

# @app.post("/submit/")
# def submit_form(form_data: MyForm):
#     return {"name": form_data.name, "email": form_data.email}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

import requests

url = "http://0.0.0.0:3000/login"
params = {"email":"a@abc.com", "password":"abc"}

response = requests.get(url, params=params)
print(response.content)

