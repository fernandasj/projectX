from rest_framework import routers

from . import api_views as api

app_name = 'exams-api'

router = routers.DefaultRouter()
router.register(r'exams', api.QuestionViewSet, base_name='api-exams')
router.register(r'discipline', api.DisciplineViewSet, base_name='api-exams')

urlpatterns = router.urls