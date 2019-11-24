from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend.schedule import views

router = DefaultRouter()
router.register(r'issue', views.IssueViewSet)
router.register(r'issues/answer', views.AnswerOnIssueViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('help/answer/<id>', include(router.urls)),
]
