
"""
    Main training workflow
"""
from flask import Flask, request
from runner import call_train
from flask import make_response
import json

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
    with open('/home/ubuntu/Capstone_Project/PreSumm/raw_data/temp.raw_src', 'w') as f:
        f.write(sentence)
    call_train()
    text = ''
    with open('/home/ubuntu/Capstone_Project/PreSumm/logs/abs_bert_cnndm_step-1.candidate', 'r') as f:
        text = f.read()
    print("Success!!")
    return text


@app.route('/hello')
def other_page():
    response = make_response('The page named does not exist.', 404)
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
