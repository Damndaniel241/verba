"""
ASGI config for verba project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
# from chat.middleware import JwtAuthMiddleware,JwtAuthMiddlewareStack
from chat.middleware2 import JWTAuthMiddleware


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'verba.settings')

# application = get_asgi_application()
django_asgi_app = get_asgi_application()
from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http":django_asgi_app,
    # "websocket":
    #     AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    
    # "websocket":AllowedHostsOriginValidator(
    #     AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    # )
    # "websocket": JwtAuthMiddleware(
    #     URLRouter(websocket_urlpatterns)
    # )
    # "websocket": AllowedHostsOriginValidator(
    #             JwtAuthMiddlewareStack(
    #                 URLRouter(websocket_urlpatterns)
    #             )
    #         ),
    #  "websocket": AllowedHostsOriginValidator(
        "websocket":
        JWTAuthMiddleware(
            URLRouter(websocket_urlpatterns)
        ),
    # ),
})

