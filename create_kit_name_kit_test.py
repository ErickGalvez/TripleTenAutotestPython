from tkinter.font import names

import requests
import data
import configuration

kit_body = data.kit_body.copy()
user_body = data.user_body.copy()

def create_user(body):
    request = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,"",body)
    print(request.json())
    return request.json()

def get_token(request):
    body_token = 'Bearer ' + request.get("authToken")

    auth_token = {
    "Content-Type" : "application/json",
    "Authorization": body_token
    }

    return auth_token

def create_kit(kit_name):
    print("creating kit with kit name:" + kit_name["name"])
    token = get_token(create_user(user_body))
    print("token is "+ token["Authorization"])
    response_kit = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,json = kit_name,headers = token)
    return response_kit

def change_kit_body(kit_name):
    print("current default kit name: " + kit_body["name"])
    print("changing to " + kit_name)
    kit_body["name"] = kit_name
    return kit_body

def kit(kit_string):
    kit_name = change_kit_body(kit_string)
    response = create_kit(kit_name)
    return response.status_code

def create_empty_kit(): #special function to insert empty json as parameter
    token = get_token(create_user(user_body))
    response_kit = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,json = {},headers = token)
    return response_kit

def create_number_kit(): #special function to insert int number in "name"
    token = get_token(create_user(user_body))
    response_kit = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json={"name" : 123}, headers=token)
    return response_kit

def positive_assert(name):
    assert kit(name) == 201
def negative_assert(name):
    assert kit(name) == 400

def test_two_letter_kit_name():
    positive_assert("aa")
def test_five_one_one_letter_kit_name():
    positive_assert(data.name_five_one_one)
def test_empty_letter_kit_name():
    negative_assert("")
def test_five_one_two_letter_kit_name():
    negative_assert(data.name_five_one_two)
def test_special_character_kit_name():
    positive_assert("\"№%@\",")
def test_space_kit():
    positive_assert("A Aaa ")
def test_number_kit_name():
    positive_assert("123")
def test_no_name():
    assert create_empty_kit().status_code == 400
def test_int_name():
    assert create_number_kit().status_code == 400