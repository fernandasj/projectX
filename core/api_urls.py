from rest_framework import routers

from . import api_views as api

app_name = 'core-api'

router = routers.DefaultRouter()
router.register(r'core', api.TeacherViewSet, base_name='api-core')

urlpatterns = router.urls