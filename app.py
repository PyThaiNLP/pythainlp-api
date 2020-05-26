# -*- coding: utf-8 -*-
from fastapi import Depends, FastAPI, Header, HTTPException
from routers import tag, tokenize

app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}


app.include_router(tag.router)
app.include_router(tokenize.router)
