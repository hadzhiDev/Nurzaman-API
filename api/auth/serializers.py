from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from accounts.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(email=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError("Неверный email или пароль")

        token, _ = Token.objects.get_or_create(user=user)
        return {"token": token.key, "email": user.email}
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'full_name', "password", "password2")

    def validate(self, attrs):
        if not attrs['password'] == attrs['password2']:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        Token.objects.create(user=user)
        return validated_data



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "full_name", "phone_number")
        read_only_fields = ("email",)


class FunctionChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate(self, attrs):
        user = self.context["request"].user
        print(attrs.get("old_password"))
        print(attrs.get("new_password"))
        if not user.check_password(attrs.get("old_password")):
            raise serializers.ValidationError("Старый пароль неверен")
        return attrs
    
    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user
    


class GenericChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate(self, attrs):
        user = self.context["request"].user
        print(attrs.get("old_password"))
        print(attrs.get("new_password"))
        if not user.check_password(attrs.get("old_password")):
            raise serializers.ValidationError("Старый пароль неверен")
        return attrs


class DeactivateSerializer(serializers.Serializer):
    confirm = serializers.BooleanField(required=True)