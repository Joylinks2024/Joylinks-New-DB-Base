from django.urls import path

from .views import Courses_List, Courses_Title_List, Courses_Count_List

urlpatterns = [
    path('get/', Courses_List),
    path('title/', Courses_Title_List),
    path('count/', Courses_Count_List),
]
