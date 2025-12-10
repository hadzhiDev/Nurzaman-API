from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .api import apartmens_list, apartmens_create, apartment_detail, objects_list
from .class_api import ApartmentViewSet, ObjectViewSet

router = DefaultRouter()
router.register('apartments', ApartmentViewSet, basename='apartments')
router.register('objects', ObjectViewSet, basename='objects')


urlpatterns = [
    path('', include(router.urls))
    # path('apartments-list/', apartmens_list, name='apartments-list'),
    # path('apartments-create/', apartmens_create, name='apartments-create'),
    # path('apartment-detail/<int:pk>/', apartment_detail, name='apartment-detail'),

    # path('objects-list/', objects_list,),
]