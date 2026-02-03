from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessionalViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'profissionais', ProfessionalViewSet)
router.register(r'consultas', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# Endereço das views