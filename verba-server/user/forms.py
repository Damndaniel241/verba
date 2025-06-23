from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import NewUser


class NewUserCreationForm(UserCreationForm):

    class Meta:
        model = NewUser
        fields = ("email","user_name",)


class NewUserChangeForm(UserChangeForm):

    class Meta:
        model = NewUser
        fields = ("email","user_name")