from django.urls import path
from backend.schedule import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'help', views.HelpViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

