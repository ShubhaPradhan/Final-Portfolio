from django.db import models

# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=100)
    resume =  models.FileField(upload_to='resume')

    def __str__(self):
        return self.name