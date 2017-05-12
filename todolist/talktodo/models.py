from django.db import models
from datetime import datetime
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    checked = models.BooleanField()