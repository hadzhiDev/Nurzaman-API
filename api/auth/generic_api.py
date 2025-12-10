from rest_framework.generics import (GenericAPIView, CreateAPIView, ListAPIView, DestroyAPIView, 
                                     RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from accounts.models import User
from .serializers import RegisterSerializer, ProfileSerializer, LoginSerializer, GenericChangePasswordSerializer, DeactivateSerializer
    

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ChangePasswordView(GenericAPIView):
    serializer_class = GenericChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)

        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()

        return Response({"message": "Пароль успешно изменён"})


class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({"message": "Вы вышли из системы"})


class DeactivateAccountView(GenericAPIView):
    serializer_class = DeactivateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not serializer.validated_data['confirm']:
            return Response({"error": "Подтвердите деактивацию"}, status=400)

        request.user.is_active = False
        request.user.save()

        return Response({"message": "Аккаунт деактивирован"})