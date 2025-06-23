# from urllib.parse import parse_qs
# from jwt import decode as jwt_decode
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# from rest_framework_simplejwt.tokens import UntypedToken
# from django.contrib.auth import get_user_model
# from django.conf import settings
# from channels.db import database_sync_to_async

# User = get_user_model()

# @database_sync_to_async
# def get_user(user_id):
#     try:
#         return User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         return None

# class JWTAuthMiddleware:
#     def __init__(self, inner):
#         self.inner = inner
        
        

#     def __call__(self, scope):
#         return JWTAuthMiddlewareInstance(scope, self)

# class JWTAuthMiddlewareInstance:
#     def __init__(self, scope, middleware):
#         self.scope = scope
#         self.middleware = middleware

#     async def __call__(self, receive, send):
#         query_string = self.scope["query_string"].decode()
#         token = parse_qs(query_string).get("token", [None])[0]

#         self.scope["user"] = None  # default to anonymous

#         if token:
#             try:
#                 UntypedToken(token)  # verifies signature, exp, etc.
#                 decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#                 user_id = decoded_data.get("user_id")

#                 user = await get_user(user_id)
#                 if user:
#                     self.scope["user"] = user
#                     print("[Middleware] user =", user)

#             except (TokenError, InvalidToken, Exception) as e:
#                 print("JWT WebSocket auth failed:", e)
#                 self.scope["user"] = None

#         inner = self.middleware.inner(self.scope)
#         return await inner(receive, send)


from urllib.parse import parse_qs
from jwt import decode as jwt_decode
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth import get_user_model
from django.conf import settings
from channels.db import database_sync_to_async

User = get_user_model()

@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None

class JWTAuthMiddleware:
    def __init__(self, app):
        self.app = app  # This is your inner ASGI app (like URLRouter)

    async def __call__(self, scope, receive, send):
        query_string = scope["query_string"].decode()
        token = parse_qs(query_string).get("token", [None])[0]

        scope["user"] = None  # default

        if token:
            try:
                UntypedToken(token)
                decoded = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                user_id = decoded.get("user_id")
                user = await get_user(user_id)

                if user:
                    scope["user"] = user
            except (InvalidToken, TokenError, Exception) as e:
                print("WebSocket JWT auth failed:", e)

        return await self.app(scope, receive, send)
