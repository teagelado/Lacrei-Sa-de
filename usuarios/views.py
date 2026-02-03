from rest_framework import viewsets
from .models import Professional, Appointment
from .serializers import ProfessionalSerializer, AppointmentSerializer


class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    #requisições da internet e entrega os dados