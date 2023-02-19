from fastapi import FastAPI

app = FastAPI()

# "/"にGETメソッドでリクエストした際の処理を定義
@app.get("/")
def index():
    return {"Hello": "World"}

# "/items/{item_id}"にGETメソッドでリクエストした際の処理を定義
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
