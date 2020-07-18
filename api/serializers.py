from rest_framework import serializers
from .models import Question, Subject, Option

class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = ['id', 'subject_name']

class OptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Option
        fields = ['option','is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    subject = SubjectSerializer(many=False)
    class Meta:
        model = Question
        fields = ['subject','id', 'question', 'options']




