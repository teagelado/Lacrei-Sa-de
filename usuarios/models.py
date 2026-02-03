from django.db import models

class Professional(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    date = models.DateTimeField()
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)

   
    def __str__(self):
        return f"Consulta com {self.professional.name} em {self.date}"

        #define as tabelas