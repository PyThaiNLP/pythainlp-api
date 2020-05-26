# -*- coding: utf-8 -*-
from fastapi import Depends, FastAPI, Header, HTTPException
from routers import tag, tokenize
from pythainlp import __version__

app = FastAPI()


@app.get("/")
def hello():
    return {"pythainlp": __version__}


app.include_router(tag.router)
app.include_router(tokenize.router)
