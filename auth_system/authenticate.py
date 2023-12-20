from rest_framework_simplejwt import authentication as jwt_authentication
from django.conf import settings
from rest_framework import authentication, exceptions as rest_exceptions




## TODO: Enhcement would be better to check enforce_csrf coming from the user too.
# def enforce_csrf(request):
#     check = authentication.CSRFCheck(request)
#     reason = check.process_view(request, None, (), {})
#     if reason:
#       raise rest_exceptions.PermissionDenied('CSRF Failed: %s' % reason)


class CustomAuthentication(jwt_authentication.JWTAuthentication):
    def getRequestHeaders(self, string, request):
        if request.headers:
            if string in request.headers:
                return request.headers[string]
            else:
                return False
        else:
            return None

    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None

        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token

