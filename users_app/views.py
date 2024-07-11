from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import Bot_Users, UserSerializer, PermissionSerializer, UserBanSerializer, UserActiveSerializer, \
    Update_Course_Serializer
from .serializers import PersonalDataSerializer, UpdateFirstNameSerializer, UpdateLastNameSerializer
from .serializers import UpdateAdminSerializer
from .serializers import UpdateRegionSerializer, UpdateDistrictSerializer, UpdatePhoneNumberSerializer


@api_view(['GET', 'POST'])
def User_List(request):
    if request.method == 'GET':
        snippets = Bot_Users.objects.filter(is_active=True)
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def NextTopSoreUserList(request):
#     if request.method == 'GET':
#         snippets = Bot_User.objects.filter(is_active=True, total_score__gte=60).order_by('-total_score',
#                                                                                          '-create_time')[
#                    :20]
#         serializer = UserSerializer(snippets, many=True)
#         ser_data = serializer.data[10:20]
#         if len(ser_data) <= 9:
#             ser_data = []
#         return Response(ser_data)


@api_view(['GET', 'PUT', 'DELETE'])
def User_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def Permission_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)

    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PermissionSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PermissionSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def User_Ban_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserBanSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserBanSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def User_Active_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserActiveSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserActiveSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def Personal_Data_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonalDataSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonalDataSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def First_Name_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateFirstNameSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateFirstNameSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def Last_Name_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateLastNameSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateLastNameSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def Region_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UpdateRegionSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateRegionSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def District_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)

    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateDistrictSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateDistrictSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def Phone_Number_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdatePhoneNumberSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdatePhoneNumberSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Admin_Count_List(request):
    if request.method == 'GET':
        if request.data:
            snippets = Bot_Users.objects.filter(is_active=True, is_admin=request.data['is_admin'])
            serializer = UserSerializer(snippets, many=True)
            return Response({"count": len(serializer.data),
                             "data": serializer.data})
        else:
            snippets = Bot_Users.objects.filter(is_active=True, is_admin="A")
            serializer = UserSerializer(snippets, many=True)
            return Response({"count": len(serializer.data),
                             "data": serializer.data})


@api_view(['GET', 'PUT'])
def Admin_Detail(request, tg_id):
    """
    :param request: {"is_admin":"A"}
    :param tg_id: {"tg_id":1234}
    :return: if is_avlid: {"is_admin":"A"}
             else: HTTP_404_NOT_FOUND or HTTP_400_BAD_REQUEST
    """
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id, is_active=True)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateAdminSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateAdminSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Users_Count_List(request):
    if request.data:
        if "call_state" in request.data and "off_state" in request.data:
            snippets_call_state = Bot_Users.objects.filter(call_state__gte=request.data['call_state'])
            snippets_off_state = Bot_Users.objects.filter(off_state__gte=request.data['off_state'])
            serializer_call_state = UserSerializer(snippets_call_state, many=True)
            serializer_off_state = UserSerializer(snippets_off_state, many=True)
            return Response(data={"call_state": len(serializer_call_state.data),
                                  "off_state": len(serializer_off_state.data)})
        if type(request.data[list(request.data.keys())[0]]) != int:
            return Response(data=f"Type Error: {request.data[list(request.data.keys())[0]]} !",
                            status=status.HTTP_400_BAD_REQUEST)
        if "call_state" in request.data:
            snippets = Bot_Users.objects.filter(call_state__gte=request.data['call_state'])
            serializer = UserSerializer(snippets, many=True)
        elif "off_state" in request.data:
            snippets = Bot_Users.objects.filter(off_state__gte=request.data['off_state'])
            serializer = UserSerializer(snippets, many=True)
        else:
            return Response(data=f"{list(request.data.keys())} not found !", status=status.HTTP_404_NOT_FOUND)
        return Response(data={list(request.data.keys())[0]: len(serializer.data)}, status=status.HTTP_200_OK)

    snippets_true = Bot_Users.objects.filter(is_active=True)
    snippets_false = Bot_Users.objects.filter(is_active=False)
    serializer_true = UserSerializer(snippets_true, many=True)
    serializer_false = UserSerializer(snippets_false, many=True)
    return Response(data={True: len(serializer_true.data),
                          False: len(serializer_false.data)}, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def Register_User_Detail(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        if "course_id" not in request.data:
            return Response(data="Metod Not Allowed !", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = Update_Course_Serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_user = UserSerializer(user)
            return Response(serializer_user.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def Register_User_Detail_Clear(request, tg_id):
    try:
        user = get_object_or_404(Bot_Users, tg_id=tg_id)
    except Exception as e:
        return Response({'error': f'User not found: {str(e)}'}, status=status.HTTP_404_NOT_FOUND)
    if 'course_ids' in request.data:
        course_ids = request.data['course_ids']
        if isinstance(course_ids, list):
            try:
                user.course_id.remove(*course_ids)
                user.save()
                serializer_user = UserSerializer(user)
                return Response(serializer_user.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'course_ids must be a list'}, status=status.HTTP_400_BAD_REQUEST)
    elif 'course_id' in request.data:
        if isinstance(request.data['course_id'], str):
            try:
                user.course_id.remove(request.data['course_id'])
                user.save()
                serializer_user = UserSerializer(user)
                return Response(serializer_user.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    elif {} == request.data:
        try:
            user.course_id.clear()
            user.save()
            serializer_user = UserSerializer(user)
            return Response(serializer_user.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'course_ids or course_id not provided'}, status=status.HTTP_400_BAD_REQUEST)
