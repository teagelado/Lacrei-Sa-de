from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Professional

class ProfessionalTest(APITestCase):
    def test_create_professional(self):
        # rota que o Router criou é 'professional-list'
        url = '/api/profissionais/' 
        data = {
            'name': 'Dr. João', 
            'specialty': 'Cardiologia', 
            'address': 'Rua Exemplo, 123', 
            'contact': '1199999999'
        }
        response = self.client.post(url, data, format='json')
        
        # Verifica se o código de resposta é 201 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #verificação de erros