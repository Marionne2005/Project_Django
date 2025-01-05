from django.db import models

class Task(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    priority=models.CharField(max_length=50)

    objects=models.Manager()
    def __str__(self):
         return self.title