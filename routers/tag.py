# -*- coding: utf-8 -*-
from fastapi import APIRouter
from pythainlp import tag

router = APIRouter()


@router.get("/tag/pos_tag", tags=["tag"])
def part_of_speech_tagging(q: str, engine: str = None, corpus: str = None):
    words = pythainlp.tokenize.word_tokenize(q)
    if not engine:
        engine = "perceptron"
    if not corpus:
        corpus = "orchid"
    return tag.pos_tag(words, engine, corpus)
