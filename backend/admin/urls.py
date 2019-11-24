from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)

from backend.admin import views

router = DefaultRouter()
router.register(r'notifications', views.NotificationViewSet)

urlpatterns = [
    path('requests/<type>', views.RequestList.as_view(), name='request_list'),
    path('requests/groupby/state/<type>', views.RequestGroupByList.as_view(), name='request_list'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
