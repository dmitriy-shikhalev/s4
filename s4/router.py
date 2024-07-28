from fastapi import FastAPI

app = FastAPI(title='router')


@app.get("/ping", status_code=200)
def ping():
    return "pong"
