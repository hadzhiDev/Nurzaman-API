from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .serializers import ApartmentListSerializer, ObjectSerializer, ApartmentDetailSerializer
from main.models import Apartment, Object


@api_view(['GET'])
def objects_list(request):
    objects = Object.objects.all()
    print(objects.count())

    paginator = PageNumberPagination()
    paginator.page_size = 2

    result_page = paginator.paginate_queryset(objects, request)
    serializer = ObjectSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def apartmens_list(request):
    apartments = Apartment.objects.all()
    serializer = ApartmentListSerializer(apartments, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def apartmens_create(request):
    serializer = ApartmentDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    print(serializer.errors)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def apartment_detail(request, pk):
    try:
        apartment = Apartment.objects.get(pk=pk)
    except Apartment.DoesNotExist:
        return Response({"datail": "Not Fount"})

    if request.method == "GET":
        serializer = ApartmentDetailSerializer(apartment, many=False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = ApartmentDetailSerializer(apartment, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":
        apartment.delete()
        return Response(status=204)
