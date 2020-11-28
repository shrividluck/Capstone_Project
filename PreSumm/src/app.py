
"""
    Main training workflow
"""
from flask import Flask, request
from runner import call_train
from flask import make_response
import json
import os
from train_extractive import train_ext, validate_ext, test_ext, test_text_ext, test_text_ext_from_string

app = Flask(__name__)
model, args, trainer = call_train()


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

    text = test_text_ext_from_string(args, model, trainer, sentence)

    print("Success!!")
    return text if text else 'Something went wrong :-('


@app.route('/hello')
def other_page():
    response = make_response('The page named does not exist.', 404)
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
