from rest_framework import serializers
from .models import NewUser,Profile
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.contrib.auth import authenticate

class NewUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = NewUser
        fields= ('id','email','user_name','password2','password')
        
    
    def validate(self, attr):
        password = attr.get("password")
        password2 = attr.pop("password2")
        if password != password2:
            raise serializers.ValidationError("passwords do not match!")
        return attr
        
    def validate_user_name(self, value):
        if NewUser.objects.filter(user_name=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")  # Custom message
        elif value.count(" ")>0:
            raise serializers.ValidationError("username shouldn't have space")
        return value
 
    def validate_email(self, value):
        if NewUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email address already exists.")  # Custom message
        return value
        
    
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        # user = super().create(validated_data)
        user = NewUser(**validated_data)
        user.set_password(password) 
        user.save()
        profile = Profile.objects.create(user=user)
        profile.save()
        return user
    
    

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validate_email])
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
        
    class Meta:
        model = NewUser
        fields = ("email","password",)
    def validate(self, data):
        user = authenticate(**data)
        if user is not None:
            return user
        raise Exception("email or password is incorrect")
        