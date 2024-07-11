from rest_framework.serializers import ModelSerializer

from .models import Courses


class Courses_Serializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class Update_Courses_Serializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = ['info', 'photo', 'is_active']


class Update_Courses_Title_Serializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = ['title']
