from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentView

router = DefaultRouter()
router.register(r'', AppointmentView)

urlpatterns = [
    path('', include(router.urls)),
]