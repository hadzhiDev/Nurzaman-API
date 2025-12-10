from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import LoginSerializer, ProfileSerializer, FunctionChangePasswordSerializer, RegisterSerializer



@api_view(["POST"])
@permission_classes([AllowAny])
def custom_login(request):
    serialiser = LoginSerializer(data=request.data)
    serialiser.is_valid(raise_exception=True)

    return Response(serialiser.validated_data)


@api_view(["POST"])
@permission_classes([AllowAny])
def custom_register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    print(request.user)
    Token.objects.filter(user=request.user).delete()
    return Response({"detail": "Successfully logged out."})


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    if request.method == "GET":
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    if request.method in ["PUT", "PATCH"]:
        serializer = ProfileSerializer(user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = FunctionChangePasswordSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"detail": "Password changed successfully."})
    