from django.urls import path
from .views import signup,signin,logout,retrieveUsers,retrieveSingleUser

urlpatterns = [
    path("signup/",signup),
    path("signin/",signin),
    path("logout/",logout),
    path("users/",retrieveUsers),
    path("users/<int:pk>/",retrieveSingleUser)
]