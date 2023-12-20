from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.middleware import csrf
from auth_system.models import CustomUser
from django.utils.deprecation import MiddlewareMixin


class CustomHeaderMiddleware(MiddlewareMixin):

    """Middleware"""

    """
    Main functionality
    1- Check if the user already has a token for this system
    2- if
        - Yes will update with a newly refreshed token in the request header and handle that in the Next middleware
            - For this case they user will never go expire except request LOGOUT
        - NO will do nothing
    """
    def process_request(self, request):
        if 'Token_Updated' in request.headers:
            request.META['HTTP_TOKEN_UPDATED'] = False
            print('Can not get there buddy hahaha')



        raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None

        if raw_token is not None:
                try:
                    # get the token payload to get user id ##### For valid token
                    payload = jwt.decode(raw_token, settings.SECRET_KEY, algorithms=['HS256'])
                except:
                    # get the token payload to get user id ##### For our system unvalid token
                    payload = jwt.decode(raw_token, settings.SECRET_KEY, algorithms=['HS256'], options={"verify_signature": False})


                    ################################################################
                    ################### Validate the expired Cookies with the user_id is in our system  ###############################
                    #TODO: enhance to return the right Error message #########################
                    try:
                        user_id = payload['user_id']
                        user = CustomUser.objects.get(id=user_id)
                    except Exception as er:
                        raise er



                    # Create a new re
                    refresh = RefreshToken.for_user(user)
                    raw_token_new = refresh.access_token
                    raw_token_new['first_name'] = user.first_name
                    raw_token_new['last_name'] = user.last_name
                    raw_token_new['email'] = user.email
                    request.COOKIES[settings.SIMPLE_JWT['AUTH_COOKIE']] = str(raw_token_new)
                    # HTTP_TOKEN_UPDATED is just a parameter used for the next coming request to validate the user is authorized
                    request.META['HTTP_TOKEN_UPDATED'] = True


class CustomAssingCookieMiddleware:

    def getRequestHeaders(self, string, request):
        if request.headers:
            if string in request.headers:
                return request.headers[string]
            else:
                return False
        else:
            return False

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.


        response = self.get_response(request)
        updated = self.getRequestHeaders('Token_Updated', request)
        if updated:
            access = request.COOKIES['access']
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=access,
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )

        return response