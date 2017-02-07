from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from hive.models import Drone
from .models import WhiteBall, RedBall


class PowerBallModelTest(TestCase):
    def setUp(self):
        self.drone = Drone.objects.create(first_name='wade', last_name='wilson')

    def test_white_ball_can_be_assigned_all_legal_values(self):
        for value in range(1, 70):
            ball = WhiteBall(value=value)
            self.assertEqual(ball.value, value)

    def test_red_ball_can_be_assigned_all_legal_values(self):
        for value in range(1, 27):
            ball = RedBall(value=value)
            self.assertEqual(ball.value, value)

    def test_white_ball_raises_correct_error_with_out_of_range_value(self):
        ball = WhiteBall.objects.create(value=70, hive_drone_id=self.drone)
        self.assertRaises(ValidationError, ball.full_clean)

    def test_red_ball_raises_correct_error_with_out_of_range_value(self):
        ball = RedBall.objects.create(value=27, hive_drone_id=self.drone)
        self.assertRaises(ValidationError, ball.full_clean)

    def test_white_ball_returns_correct_error_message(self):
        ball = WhiteBall.objects.create(value=70, hive_drone_id=self.drone)
        with self.assertRaisesRegex(ValidationError,
                                    '70 is not within range 1 to 69'):
            ball.full_clean()

    def test_red_ball_returns_correct_error_message(self):
        ball = RedBall.objects.create(value=27, hive_drone_id=self.drone)
        with self.assertRaisesRegex(ValidationError,
                                    '27 is not within range 1 to 26'):
            ball.full_clean()

    def test_unique_constraint_blocks_creating_dublicate_drone_balls(self):
        self.drone.whiteball_set.create(value=1)
        self.assertRaises(IntegrityError, self.drone.whiteball_set.create,
                          value=1)

