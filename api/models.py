from django.db import models
# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length=60)

    def __str__(self):
        return self.subject_name

class Question(models.Model):
    question = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')

    def __str__(self):
        return self.question

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=80)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option
