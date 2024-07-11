from django.core import exceptions
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Courses
from .serializers import Courses_Serializer, Update_Courses_Serializer, Update_Courses_Title_Serializer


@api_view(['GET', 'POST', 'PUT'])
def Courses_List(request):
    if request.method == 'GET':
        if request.data == {}:
            snippets = Courses.objects.filter()
            serializer = Courses_Serializer(snippets, many=True)
            return Response(serializer.data)
        if "is_active" in request.data and 'id' not in request.data:
            try:
                snippets = Courses.objects.filter(is_active=request.data['is_active'])
                serializer = Courses_Serializer(snippets, many=True)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            except exceptions.ValidationError:
                return Response(data=f"IS ACTIVE not found ! -> {request.data['is_active']}",
                                status=status.HTTP_404_NOT_FOUND)
        if "is_active" in request.data and 'id' in request.data:
            try:
                snippets = Courses.objects.filter(id=request.data['id'],
                                                  is_active=request.data['is_active'])
                serializer = Courses_Serializer(snippets, many=True)
                if serializer.data:
                    return Response(serializer.data[0], status=status.HTTP_200_OK)
                else:
                    return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
            except exceptions.ValidationError:
                return Response(data=f"ID: {request.data['id']} or IS ACTIVE: {request.data['is_active']} "
                                     f"Not Found !", status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = Courses_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        try:
            course = get_object_or_404(Courses, id=request.data['id'])
        except KeyError:
            return Response(data=f"Course not found or deleted !", status=status.HTTP_404_NOT_FOUND)
        serializer = Update_Courses_Serializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def Courses_Title_List(request):
    if "id" in request.data:
        try:
            course = get_object_or_404(Courses, id=request.data['id'])
        except (KeyError, exceptions.ValidationError) as err:
            return Response(data=f"Course not found or deleted ! {err}", status=status.HTTP_404_NOT_FOUND)
        serializer = Update_Courses_Title_Serializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data="ID not found !", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Courses_Count_List(request):
    snippets_true = Courses.objects.filter(is_active=True)
    snippets_false = Courses.objects.filter(is_active=False)
    serializer_true = Courses_Serializer(snippets_true, many=True)
    serializer_false = Courses_Serializer(snippets_false, many=True)
    return Response(data={True: len(serializer_true.data),
                          False: len(serializer_false.data)})
