from django.db import models


class Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
    
