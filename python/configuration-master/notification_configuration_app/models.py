from django.db import models

class FileData(models.Model):
    scripts = models.CharField(max_length=20)
    json_file = models.FileField(upload_to='jsonfiles')


# Create your models here.
