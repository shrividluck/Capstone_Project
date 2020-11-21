
"""
    Main training workflow
"""
from flask import Flask, request
from runner import call_train
from flask import make_response
import json
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/summarize', methods=['POST'])
def call_output():
    #data = request.get_json(force=True)
    if request.is_json:
        sentence = request.get_json().get('text')
    else:
        sentence = request.values.get('text')
    if not sentence:
        sentence = ''
    print(sentence)
    with open('raw_data/temp.raw_src', 'w') as f:
        f.write(sentence+'\n')

    call_train()
    text = ''
    with open('logs/ext_bert_cnndm_step-1.candidate', 'r+') as f:
        text = f.read()
    print("Success!!")
    return text if text else 'Something went wrong :-('


@app.route('/hello')
def other_page():
    response = make_response('The page named does not exist.', 404)
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
