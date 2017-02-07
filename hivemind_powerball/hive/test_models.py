from django.test import TestCase

from .models import Drone


class DroneModelTest(TestCase):
    def setUp(self):
        self.drone = Drone(first_name='wade', last_name='wilson')

    def test_drone_full_name_property(self):
        self.assertEqual(self.drone.full_name, 'Wade Wilson')

    def test_string_representation(self):
        self.assertEqual(str(self.drone),
                         '<Drone: {}>'.format(self.drone.full_name))
