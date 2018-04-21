# -*- coding: utf-8 -*-
import flask
from pythainlp.tokenize import word_tokenize
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/word_tokenize", methods=['GET','POST'])
@app.route("/api/v1/word_tokenize", methods=['GET','POST'])
def word_tokenize_api():
	if flask.request.method == 'POST':
		source = flask.request.values.get('source')
		engine = flask.request.values.get('engine')
	else:
		source = flask.request.args.get('source')
		engine = flask.request.args.get('engine')
	if engine==None:
		engine='newmm'
	return '|'.join(word_tokenize(source,engine=engine))

if __name__ == '__main__':
    app.run()