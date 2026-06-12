from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh', TokenRefreshView.as_view()),
    path('appointment/', include('appointments.urls')),
    path('doctors/', include('doctors.urls')),
]
