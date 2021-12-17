## Basic Usage:

1. clone repo
2. cd into folder
3. copy `example.env` file to `.env` then edit environment variable values for mongo root username and password
4. run `docker compose build`
5. run `docker compose up`
6. click on (or paste into your browser) the link provided in the jupyter lab log output from the terminal window to 
access **Jupyter Lab** on [http://localhost:8888/](http://localhost:8888/)
7. **mongodb** is not accessible externally, but can be accessed by the fastAPI or Jupyter containers at the
URI `mongodb://username:password@mongodb`
8. navigate to [http://localhost:8080/](http://localhost:8080/) to access **fastAPI**
## Examples:
[http://localhost:8080/](http://localhost:8080/) executes the GET route `/` which executes read_root()`, from ./fastapi/app/main.py
```
@app.get("/")
def read_root():
    return {"Hello": "World"}
```
browser result:
```
{
Hello: "World"
}
```
http://localhost:8080/items/12345?q=testing executes the GET route `/items/{item_id}` which executes `read_item()`,
from ./fastapi/app/main.py and passes in the following parameters to the function: 
    - `12345`, an int object, as `item_id`
    - `"testing"`, a string object, as `q`
```
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
browser result:
```
{
item_id: 12345,
q: "testing"
}
```
http://localhost:8080/mongo/tarp-data?parameter=1000000 executes the GET route `/mongo/tarp-data` which 
executes `find_by_parameter_id()`, from ./fastapi/app/main.py and passes in the following parameters to the function: 
    - `1000000`, an int object, as `parameter`

```
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
```
browser result:
```
{"parameter":1000000,"results":[{"parameter":1000000,"source":{"model":"==GLWM","run":1639742400,"forecast":3600},"name":"Temperature Air","unit":"kelvin","levels":{"2m":[270,275,280,285],"900mb":[250,240,230,220]},"time_entered":"2021-12-17T19:07:45.582000","metadata":{"edited_by":"Jason","tags":["some","tags","here"]}}]}
```

## Documentation
  - Swagger Documentation is automatically created from your code
    - [http://localhost:8080/docs](http://localhost:8080/docs)
  - Alternative Documentation (Redoc)
    - [http://localhost:8080/redoc](http://localhost:8080/redoc)