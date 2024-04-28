from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('cursos_app.urls')),
    path('auth/', include('rest_framework.urls')),
]
