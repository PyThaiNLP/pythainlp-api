# -*- coding: utf-8 -*-
from fastapi import APIRouter
from pythainlp import tokenize

router = APIRouter()

@router.get('/tokenize/word_tokenize', tags=["tokenize"])
def word_tokenize(q: str, engine: str = None):
    if engine == None:
        engine='newmm'
    return '|'.join(tokenize.word_tokenize(q,engine=engine))
