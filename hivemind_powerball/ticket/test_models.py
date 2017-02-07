from django.test import TestCase

from .models import PowerBall
# from .validators import within_range
# from hive.models import Drone


class PowerBallModelTest(TestCase):
    def test_base_class_exists(self):
        self.assertIsNotNone(PowerBall())

    def test_base_class_value_can_hold_legal_value(self):
        pball = PowerBall()
        pball.ball_value = 1
        self.assertEqual(1, pball.ball_value)
