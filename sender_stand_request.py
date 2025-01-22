import requests
import configuration
import data


kit_body = data.kit_body.copy()
user_body = data.user_body.copy()


def post_user(user_request_body):
    user_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,json = user_request_body,headers=data.headers)
    return user_response

def post_kit(kit_request_body, token):
    kit_response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,json = kit_request_body,headers = token)
    return kit_response