from rest_framework.routers import DefaultRouter
from django.urls import path, include
from accounts.views import (
    StudentUserViewSet, UserTokenViewSet,
    TeacherListCreateView, TeacherDetailView
)

router = DefaultRouter()
router.register('token', UserTokenViewSet, basename='token')
router.register('student', StudentUserViewSet, basename='student')

urlpatterns = [
    path('teacher/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('', include(router.urls))
]
