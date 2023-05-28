from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


def get_user_from_token(token):
    token_auth = TokenAuthentication()
    try:
        auth_tuple = token_auth.authenticate_credentials(token)
        user = auth_tuple[0].id
        return user
    except AuthenticationFailed:
        return None
