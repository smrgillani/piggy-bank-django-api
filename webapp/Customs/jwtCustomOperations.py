import datetime
import jwt
from django.conf import settings
from rest_framework_jwt.settings import api_settings

def generate_access_token(user):

    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm=api_settings.JWT_ALGORITHM)
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm=api_settings.JWT_ALGORITHM)

    return refresh_token

def verify_refresh_token(token):
    rtr = False
    try:
        data = jwt.decode(token, settings.REFRESH_TOKEN_SECRET + "132", algorithms=[api_settings.JWT_ALGORITHM])
        rtr = True
    except jwt.ExpiredSignatureError:
        rtr = False
    except jwt.InvalidSignatureError:
        rtr = False
    return rtr