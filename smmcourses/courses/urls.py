from django.urls import path
from .views import register_course

urlpatterns = [
    path('register_course/', register_course, name='register_course'),
]


urlpatterns = [
path('add_favorite_course/int:course_id/', views.add_favorite_course, name='add_favorite_course'),
]