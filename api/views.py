from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Question, Subject
from .serializers import QuestionSerializer, SubjectSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    