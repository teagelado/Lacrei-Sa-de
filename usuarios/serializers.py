from rest_framework import serializers
from .models import Professional, Appointment

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'  

    # Validação 
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome deve ter mais de 3 letras!")
        return value

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

        #transforma os dados do banco em JSON para a API