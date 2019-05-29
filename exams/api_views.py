from rest_framework import viewsets, permissions

from . import models
from . import serializers

class DisciplineViewSet(viewsets.ModelViewSet):

    queryset = models.Discipline.objects.all()
    serializer_class = serializers.CreateDisciplineSerializer

    class Meta:
        list_serializer_class = serializers.DisciplineSerializer


class QuestionViewSet(viewsets.ModelViewSet):

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer