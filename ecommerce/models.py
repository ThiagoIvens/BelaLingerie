from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    image = models.FileField(upload_to="media/%Y/%m/%d/")