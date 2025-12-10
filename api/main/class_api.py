from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from main.models import Apartment, Object
from .serializers import ApartmentListSerializer, ObjectSerializer, ApartmentDetailSerializer, ApartmentCreateUpdateSerializer


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentListSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ApartmentDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return ApartmentCreateUpdateSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return IsAdminUser
        return super().get_permissions()


class ObjectViewSet(ReadOnlyModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer