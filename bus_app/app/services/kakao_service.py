import requests
from flask import current_app

def get_kakao_token(code):
    token_url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": current_app.config['KAKAO_CLIENT_ID'],
        "redirect_uri": current_app.config['KAKAO_REDIRECT_URI'],
        "code": code
    }
    response = requests.post(token_url, data=data)
    token_json = response.json()
    return token_json.get("access_token")

def get_kakao_user_info(access_token):
    user_info_url = "https://kapi.kakao.com/v2/user/me"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    response = requests.get(user_info_url, headers=headers)
    return response.json()
