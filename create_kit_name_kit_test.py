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
    token = get_token(create_user(user_body))
    response_kit = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,json = kit_name,headers = token)
    return response_kit

print(create_kit(kit_body).json())