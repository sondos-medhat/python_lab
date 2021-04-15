from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=100)
    active=models.BooleanField(default=False)
    creates_at= models.DateTimeField(null=True)

    def __str__ (self):
        return self.title
