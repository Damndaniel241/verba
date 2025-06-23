#number 1
# from urllib.parse import parse_qs
# from rest_framework_simplejwt.tokens import UntypedToken
# from django.contrib.auth import get_user_model
# from channels.db import database_sync_to_async
# from jwt import decode as jwt_decode
# from django.conf import settings

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
#         query_string = self.scope['query_string'].decode()
#         token = parse_qs(query_string).get('token', [None])[0]
        
#         if token:
#             try:
#                 UntypedToken(token)
#                 decoded = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#                 user = await get_user(decoded["user_id"])
#                 self.scope['user'] = user
#             except Exception:
#                 self.scope['user'] = None
#         else:
#             self.scope['user'] = None
            
#         inner = self.middleware.inner(self.scope)
#         return await inner(receive, send)
    






# #number 2

# from urllib.parse import parse_qs
# from rest_framework_simplejwt.tokens import UntypedToken
# from channels.db import database_sync_to_async
# from django.contrib.auth import get_user_model
# from jwt import decode as jwt_decode
# from django.conf import settings

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
#         return JWTAuthMiddlewareInstance(scope, self.inner)

# class JWTAuthMiddlewareInstance:
#     def __init__(self, scope, inner):
#         self.scope = scope
#         self.inner = inner

#     async def __call__(self, receive, send):
#         query_string = self.scope["query_string"].decode()
#         token = parse_qs(query_string).get("token", [None])[0]

#         self.scope["user"] = None  # Default fallback

#         if token:
#             try:
#                 UntypedToken(token)
#                 decoded = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#                 user = await get_user(decoded["user_id"])
#                 self.scope["user"] = user
#             except Exception:
#                 pass  # Invalid token, keep user as None

#         return await self.inner(self.scope, receive, send)





#number 3
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from django.conf import settings
from channels.sessions import CookieMiddleware
from channels.db import database_sync_to_async
from rest_framework_simplejwt.authentication import JWTAuthentication

import logging

logger = logging.getLogger(__name__)


class JwtAuthMiddleware:
    """
    Custom middleware for JWT authentication. Must be wrapped in CookieMiddleware.
    Adds user to scope if they have a valid JWT.
    """

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        close_old_connections()

        # cookies are in scope, since we're wrapped in CookieMiddleware
        jwt_cookie = scope["cookies"].get(settings.SIMPLE_JWT['AUTH_COOKIE'])

        if not jwt_cookie:
            scope["user"] = AnonymousUser()
        else:
            try:
                auth = JWTAuthentication()
                validated_token = auth.get_validated_token(jwt_cookie)
                scope["user"] = await database_sync_to_async(auth.get_user)(
                    validated_token
                )
            except Exception as e:
                # or raise validation errors, etc
                scope["user"] = AnonymousUser()

        return await self.inner(scope, receive, send)


def JwtAuthMiddlewareStack(inner):
    '''
    Handy shortcut to ensure we're wrapped in CookieMiddleware.
    Use in your ASGI application as follows:
    application = ProtocolTypeRouter(
        {
            "http": django_asgi_app,
            "websocket": AllowedHostsOriginValidator(
                JwtAuthMiddlewareStack(
                    URLRouter(websocket_urlpatterns)
                )
            ),
        }
    )
    '''
    return CookieMiddleware(JwtAuthMiddleware(inner))