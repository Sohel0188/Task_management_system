from django.db import models
from Category.models import Category

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField()
    category = models.ManyToManyField(Category)
    
    def __str__(self) -> str:
        return f"{self.title}-> {self.assign_date}"