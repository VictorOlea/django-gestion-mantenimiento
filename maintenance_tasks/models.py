from django.db import models

# Create your models here.
class Maintenance_Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    responsible = models.CharField(max_length=100)
    status = models.CharField(default="Pendiente")