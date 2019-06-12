from django.urls import path
from rest_framework import routers

from . import api_views as api

app_name = 'core-api'

router = routers.DefaultRouter()
router.register(r'teachers', api.TeacherViewSet, base_name='api-teacher')
router.register(r'students', api.StudentViewSet, base_name='api-student')

urlpatterns = router.urls

urlpatterns += [
    path('auth/', api.AuthToken.as_view()),
]