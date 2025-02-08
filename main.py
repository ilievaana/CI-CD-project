from fastapi import FastAPI
from routes.customer import customer
from routes.article import article
from routes.category import category
from config.db import conn

app = FastAPI(title="My Online Store", description="A FastAPI-based application for managing an online store with CI/CD capabilities.")


@app.get("/")
def read_root():
    return {"message": "Welcome to My Online Store! Start exploring our articles!"}


app.include_router(customer, prefix="/customers")

app.include_router(article, prefix="/articles")

app.include_router(category, prefix="/categories")