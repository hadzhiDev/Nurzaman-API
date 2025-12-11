from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from main.models import Apartment, Object
from .serializers import ApartmentListSerializer, ObjectSerializer, ApartmentDetailSerializer, ApartmentCreateUpdateSerializer
from .paginations import StandardResultsSetPagination


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentListSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('floor', 'area', 'block__name', 'block__object__name', 'type', 'rooms_count')
    filterset_fields = {
        'area': ['gte', 'lte'],   # area__gte=50, area__lte=100
        'name': ['icontains'],    # name__icontains=проспект
    }

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ApartmentDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return ApartmentCreateUpdateSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()


class ObjectViewSet(ReadOnlyModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
