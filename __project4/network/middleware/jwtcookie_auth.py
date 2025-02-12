from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CookieJWTAuthentication(JWTAuthentication): 
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)  

    def authenticate(self, request):
            # Get the access token from the cookies
            access_token = request.COOKIES.get('access')
            print(access_token)
            if access_token is None:
                return None  # No token found in cookies
            
            # self.get_raw_token(??? header)
            
            # what does self get validated?

            validated_token = self.get_validated_token(access_token)
            print(validated_token)
            return self.get_user(validated_token), validated_token
            # If the token is valid, return the user and token

    # def get_validated_token(self, raw_token: bytes) -> Token:
    #     """
    #     Validates an encoded JSON web token and returns a validated token
    #     wrapper object.
    #     """
    #     messages = [§]
    #     for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
    #         try:
    #             return AuthToken(raw_token)
    #         except TokenError as e:
    #             messages.append(
    #                 {
    #                     "token_class": AuthToken.__name__,
    #                     "token_type": AuthToken.token_type,
    #                     "message": e.args[0],
    #                 }
    #             )

    #     raise InvalidToken(
    #         {
    #             "detail": _("Given token not valid for any token type"),
    #             "messages": messages,
    #         }
    #     )


