from functools import partial

from django.core.exceptions import ValidationError


def has_duplicates(a_list):
    unique = set(a_list)
    if len(unique) != len(a_list):
        return True


def _within_range(value, lowbound, highbound):
    if value not in range(lowbound, highbound + 1):
        raise ValidationError('{} is not within range {} to {} (inclusive)'
                              .format(value, lowbound, highbound))


within_white_range = partial(_within_range, lowbound=1, highbound=69)
within_red_range = partial(_within_range, lowbound=1, highbound=26)

