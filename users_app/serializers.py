from rest_framework.serializers import ModelSerializer

from .models import Bot_Users


class UserSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = "__all__"


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['is_admin']


class UserBanSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['is_ban']


class UserActiveSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['is_active']


class PersonalDataSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['first_name', 'last_name', 'region', 'district', 'phone_number']


class UpdateFirstNameSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['first_name']


class UpdateLastNameSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['last_name']


class UpdateRegionSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['region']


class UpdateDistrictSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['district']


class UpdatePhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['phone_number']


class UpdateAdminSerializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['is_admin']


class Update_Course_Serializer(ModelSerializer):
    class Meta:
        model = Bot_Users
        fields = ['course_id', "call_state", "off_state"]
