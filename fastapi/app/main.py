import os
import urllib.parse

from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/mongo/tarp-data")
def find_by_parameter_id(parameter: int):
    username = urllib.parse.quote_plus(os.environ["MONGO_INITDB_ROOT_USERNAME"])
    password = urllib.parse.quote_plus(os.environ["MONGO_INITDB_ROOT_PASSWORD"])
    mongo_host = "mongodb"
    client = MongoClient(f"mongodb://{username}:{password}@{mongo_host}")
    db = client["tarp-data"]
    collection = db["tarp-params"]
    result = [
        record
        for record in collection.find(
            {"parameter": parameter}, projection={"_id": False}
        )
    ]

    return {"parameter": parameter, "results": result}
