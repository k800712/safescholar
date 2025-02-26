import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Kakao API 설정
    KAKAO_APP_KEY = os.getenv('KAKAO_APP_KEY', 'your_kakao_app_key_here')
    KAKAO_CLIENT_ID = os.getenv('KAKAO_CLIENT_ID')
    KAKAO_REDIRECT_URI = os.getenv('KAKAO_REDIRECT_URI')
    KAKAO_OAUTH_URL = f"https://kauth.kakao.com/oauth/authorize?client_id={KAKAO_CLIENT_ID}&redirect_uri={KAKAO_REDIRECT_URI}&response_type=code"
    KAKAO_LOGOUT_URL = f"https://kauth.kakao.com/oauth/logout?client_id={KAKAO_CLIENT_ID}&logout_redirect_uri={os.getenv('KAKAO_LOGOUT_REDIRECT_URI')}"

    # Redis 설정
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
    REDIS_DB = int(os.getenv('REDIS_DB', 0))

    # 추가 설정
    DEBUG = os.getenv('FLASK_DEBUG', 'False') == 'True'
    TESTING = False

    # 기타 필요한 설정들을 여기에 추가할 수 있습니다.
