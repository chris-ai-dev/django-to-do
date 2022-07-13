from django.db import models

# Create your models here.
# models and get started! Let's say a Todo item has a title and description
class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()