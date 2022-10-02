from http import client
from fastapi import Body
import pytest
import requests
import json


def test_root():
    resp = requests.get(url='http://localhost:8000/')
    print(str(resp.content.decode()))
    assert resp.status_code == 200
    assert resp.content.decode() == '{"message":"Fast API in Python"}'


def test_read_user_1():
    resp = requests.get(url='http://localhost:8000/user')
    data= '[{"id":1,"name":"MÃ¡rcio","mail":"example@mail.com","phone":"98769878"},{"id":2,"name":"Leandro","mail":"example_leandro@mail.com","phone":"94435676"}]'
    assert resp.status_code == 200
    assert resp.content.decode() == data


question = [
'{"id":1,"position":1,"question":"Which car model/category are you looking for?"}',
'{"id":3,"position":2,"question":"What type of fuel is your ideal car?"}',
'{"id":2,"position":3,"question":"How much money do you intend to invest in your new car?"}',
'{"detail":"Error"}'
]

def test_read_questions1():
    url="http://localhost:8000/question/1"
    resp = requests.get(url)
    assert resp.status_code == 200
    assert resp.content.decode() == str(question[0])

def test_read_questions2():
    url="http://localhost:8000/question/2"
    resp = requests.get(url)
    assert resp.status_code == 200
    assert resp.content.decode() == str(question[1])

def test_read_questions3():
    url="http://localhost:8000/question/3"
    resp = requests.get(url)
    assert resp.status_code == 200
    assert resp.content.decode() == str(question[2])

def test_read_questions_error():
    url="http://localhost:8000/question/999999"
    resp = requests.get(url)
    assert resp.status_code == 400
    assert resp.content.decode() == question[3]


questionid=[
    '[{"id":1,"question_id":1,"alternative":"compact"},{"id":2,"question_id":1,"alternative":"utilitary"},{"id":3,"question_id":1,"alternative":"sporting"},{"id":4,"question_id":1,"alternative":"suv"}]',
    '[{"id":5,"question_id":2,"alternative":"low"},{"id":6,"question_id":2,"alternative":"average"},{"id":7,"question_id":2,"alternative":"high"}]',
    '[{"id":8,"question_id":3,"alternative":"electric"},{"id":9,"question_id":3,"alternative":"fossil"},{"id":10,"question_id":3,"alternative":"bio"}]',
    '[]'
]

def test_read_alternatives_1():
    url="http://localhost:8000/alternatives/1"
    resp= requests.get(url)
    assert resp.status_code == 200
    assert resp.content.decode() == str(questionid[0])

def test_read_alternatives_2():
    url="http://localhost:8000/alternatives/2"
    resp= requests.get(url)
    assert resp.status_code == 200
    assert resp.content.decode() == str(questionid[1])

def test_read_alternatives_3():
    url="http://localhost:8000/alternatives/3"
    resp= requests.get(url)
    assert resp.status_code == 200
    assert resp.content.decode() == str(questionid[2])

def test_read_alternatives_4():
    url="http://localhost:8000/alternatives/4"
    resp= requests.get(url)
    assert resp.status_code == 200
    assert resp.content.decode() == str(questionid[3]) 


def test_create_answer_1():
    payload = {
    "user_id": 1,
    "answers": [
        {
            "question_id": 1,
            "alternative_id": 3
        },
        {
            "question_id": 2,
            "alternative_id": 2
        },
        {
            "question_id": 3,
            "alternative_id": 4
        }
    ]
    }
    url ="http://localhost:8000/answer"

    resp=requests.post(url, data=json.dumps(payload))
    assert resp.status_code == 201
    assert resp.content.decode() == '[{"id":1,"name":"Volkswagen ID.3","fuel":"electric","price":"low","category":"compact","link":""},{"id":4,"name":"Vauxhall e-Corsa","fuel":"electric","price":"low","category":"compact","link":""}]'


result=[
    '[{"user":{"id":1,"name":"MÃ¡rcio","mail":"example@mail.com","phone":"98769878"}},{"id":2,"name":"Porsche Taycan","fuel":"electric","price":"high","category":"sporting","link":""},{"id":4,"name":"Vauxhall e-Corsa","fuel":"electric","price":"low","category":"compact","link":""}]',
    '[{"id":2,"name":"Porsche Taycan","fuel":"electric","price":"high","category":"sporting","link":""},{"id":4,"name":"Vauxhall e-Corsa","fuel":"electric","price":"low","category":"compact","link":""}]'
]

def test_read_result_1():
    url ="http://localhost:8000/result/1"
    resp=requests.get(url)
    assert resp.status_code == 200
    assert resp.content.decode() == str(result[0])

def test_read_result_2():
    url ="http://localhost:8000/result/2"
    resp=requests.get(url)
    assert resp.status_code == 200
    assert resp.content.decode() == str(result[1])