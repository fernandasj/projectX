from django.urls import path

from .views import question_list

urlpatterns = [path("questions/", question_list)]