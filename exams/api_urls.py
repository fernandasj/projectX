from rest_framework import routers

from . import api_views as api

app_name = 'exams-api'

router = routers.DefaultRouter()
router.register(r'questions', api.QuestionViewSet, base_name='api-questions')
router.register(r'disciplines', api.DisciplineViewSet, base_name='api-discipline')
# router.register(r'questions/create', api.QuestionCreateView, base_name='api-question-create')
router.register(r'tests', api.TestViewSet, base_name='api-test')
router.register(r'testStudents', api.TestStudentViewSet, base_name='api-testStudents')
router.register(r'codeanswers', api.CodeAnswerViewSet, base_name='api-codeAnswer')
router.register(r'choices', api.ChoiceViewSet, base_name='api-choice')
router.register(r'answers', api.ChoiceViewSet, base_name='api-answer')


urlpatterns = router.urls