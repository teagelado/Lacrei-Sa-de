from django.contrib import admin
from .models import Professional, Appointment

admin.site.register(Professional)
admin.site.register(Appointment)

#cadastros médicos pela tela azul do Django
# salva banco de dados 

#  python manage.py makemigrations
#  python manage.py migrate
