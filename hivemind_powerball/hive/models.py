from django.urls import reverse
from django.db import models


class Drone(models.Model):
    """The users of the hive"""

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).title()

    def get_absolute_url(self):
        return reverse('hive:drone-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '<Drone: {}>'.format(self.full_name)
