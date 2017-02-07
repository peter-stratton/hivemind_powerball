from django.urls import reverse
from django.db import models

# Create your models here.
class PowerBall(models.Model):
    """The PowerBall base class"""

    ball_value = models.PositiveIntegerField()

    class Meta:
        abstract = True
