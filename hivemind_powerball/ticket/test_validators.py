from django.test import TestCase
from django.core.exceptions import ValidationError

from .validators import _within_range, within_white_range, within_red_range


class ValidatorsTest(TestCase):

    def test_within_range_validator_handles_all_legal_values(self):
        self.assertIsNone(_within_range(1, 1, 3))
        self.assertIsNone(_within_range(2, 1, 3))
        self.assertIsNone(_within_range(3, 1, 3))

    def test_within_range_validator_raises_error_for_bad_pos_value(self):
        self.assertRaises(ValidationError, _within_range,
                          value=5, lowbound=1, highbound=4)

    def test_within_range_validator_works_with_negative_ranges(self):
        self.assertIsNone(_within_range(-5, -5, 5))
        self.assertIsNone(_within_range(0, -5, 5))
        self.assertIsNone(_within_range(5, -5, 5))

    def test_within_range_validator_raises_error_for_bad_neg_value(self):
        self.assertRaises(ValidationError, _within_range,
                          value=-6, lowbound=-5, highbound=6)

    def test_within_range_validator_returns_correct_error_message(self):
        with self.assertRaisesRegex(ValidationError,
                                    '5 is not within range 1 to 4'):
            _within_range(5, 1, 4)

    def test_within_white_range_handles_all_possible_correct_values(self):
        for value in range(1, 70):
            self.assertIsNone(within_white_range(value))

    def test_within_red_range_handles_all_possible_correct_values(self):
        for value in range(1, 27):
            self.assertIsNone(within_red_range(value))

    def test_within_white_range_returns_correct_error_message_for_high(self):
        with self.assertRaisesRegex(ValidationError,
                                    '70 is not within range 1 to 69'):
            within_white_range(70)

    def test_within_white_range_returns_correct_error_message_for_low(self):
        with self.assertRaisesRegex(ValidationError,
                                    '0 is not within range 1 to 69'):
            within_white_range(0)

    def test_within_red_range_returns_correct_error_message_for_high(self):
        with self.assertRaisesRegex(ValidationError,
                                    '27 is not within range 1 to 26'):
            within_red_range(27)

    def test_within_red_range_returns_correct_error_message_for_low(self):
        with self.assertRaisesRegex(ValidationError,
                                    '0 is not within range 1 to 26'):
            within_red_range(0)




