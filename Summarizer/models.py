from django.db import models

class Text(models.Model):
    content = models.TextField()
