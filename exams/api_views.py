from rest_framework import viewsets, permissions

from . import models, serializers

# ======================
# Discipline
# ======================
class DisciplineViewSet(viewsets.ModelViewSet):

    queryset = models.Discipline.objects.all()
    serializer_class = serializers.DisciplineSerializer


# ======================
# Question
# ======================
class QuestionViewSet(viewsets.ModelViewSet):

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer