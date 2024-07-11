from django.urls import path, register_converter

from .views import District_Detail, Phone_Number_Detail, Admin_Count_List, Admin_Detail, User_List, \
    Register_User_Detail_Clear
from .views import Permission_Detail, Region_Detail, Last_Name_Detail, First_Name_Detail, Users_Count_List, \
    Register_User_Detail
from .views import User_Ban_Detail, User_Active_Detail, Personal_Data_Detail, User_Detail


class TelegramIDConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(TelegramIDConverter, 'tg_id')

urlpatterns = [
    path('users/', User_List),
    path('users/count/', Users_Count_List),
    path('users/course/<tg_id:tg_id>/get-edit/', Register_User_Detail),
    path('users/course/<tg_id:tg_id>/edit-call-off/', Register_User_Detail),
    path('users/course/<tg_id:tg_id>/clear/', Register_User_Detail_Clear),
    path('users/<tg_id:tg_id>/', User_Detail),
    path('users/<tg_id:tg_id>/permissions/', Permission_Detail),
    path('users/<tg_id:tg_id>/ban/', User_Ban_Detail),
    path('users/<tg_id:tg_id>/active/', User_Active_Detail),
    path('users/<tg_id:tg_id>/personal-data/', Personal_Data_Detail),
    path('users/<tg_id:tg_id>/first-name/', First_Name_Detail),
    path('users/<tg_id:tg_id>/last-name/', Last_Name_Detail),
    path('users/<tg_id:tg_id>/region/', Region_Detail),
    path('users/<tg_id:tg_id>/district/', District_Detail),
    path('users/<tg_id:tg_id>/phone-number/', Phone_Number_Detail),
    path('admins/', Admin_Count_List),
    path('admins/<tg_id:tg_id>/is-admin/', Admin_Detail),
]
