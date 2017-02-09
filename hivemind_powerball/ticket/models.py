# ticket/models.py
"""Model classes for Powerball balls"""

from django.db import models

from .validators import within_white_range, within_red_range


class AbstractBall(models.Model):
    """The Ball Base Class"""

    hive_drone_id = models.ForeignKey("hive.Drone", on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unique_together = ("hive_drone_id","value")


class WhiteBall(AbstractBall):
    """The White Powerball class"""

    value = models.PositiveSmallIntegerField(validators=[within_white_range])


class RedBall(AbstractBall):
    """The Red Powerball class"""

    value = models.PositiveSmallIntegerField(validators=[within_red_range])
