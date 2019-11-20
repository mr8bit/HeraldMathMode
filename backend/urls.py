from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.admin.urls')),
    path('api/', include('backend.schedule.urls')),
    path('', include('backend.bot.urls')),
]
