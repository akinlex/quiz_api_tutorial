from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, SubjectViewSet

# Create your views here.
router = DefaultRouter()
router.register('questions', QuestionViewSet, basename='questions_api')
router.register('subjects', SubjectViewSet, basename='subjects_api')

urlpatterns = router.urls