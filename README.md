Basic Usage:

1. clone repo
2. cd into folder
3. run `docker compose build`
4. run `docker compose up`
5. click on (or paste into your browser) the link provided in the jupyter lab log output from the terminal window to 
access **Jupyter Lab** on [http://localhost:8888/](http://localhost:8888/)
6. **mongodb** is not accessible externally, but can be accessed by the fastAPI or Jupyter containers at the
URI `mongodb://useradmin:boop@mongodb`
7. navigate to [http://localhost:8080/](http://localhost:8080/) to access **fastAPI**
- examples:
  - [http://localhost:8080/](http://localhost:8080/) executes the GET route `/` which executes read_root()`, from ./fastapi/app/main.py
```
@app.get("/")
def read_root():
    return {"Hello": "World"}
```
  - browser result:
```
{
Hello: "World"
}
```
  - http://localhost:8080/items/12345?q=testing executes the GET route `/items/{item_id}` which executes `read_item()`,
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
  - Swagger Documentation is automatically created from your code
    - [http://localhost:8080/docs](http://localhost:8080/docs)
  - Alternative Documentation (Redoc)
    - [http://localhost:8080/redoc](http://localhost:8080/redoc)