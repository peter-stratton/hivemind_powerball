from functools import partial

from django.core.exceptions import ValidationError


def has_duplicates(a_list):
    """Given a list of values, determines whether there are any duplicates

    Args:
        a_list (list): A list to check for duplicates

    Returns:
        bool: True if duplicates are found, False otherwise.
    """
    unique = set(a_list)
    if len(unique) != len(a_list):
        return True
    return False


def _within_range(value, lowbound, highbound):
    """Determines whether a numeric value is within a range.

    Args:
        value (int): The value in question
        lowbound (int): The lowest possible value of the range
        highbound (int): The highest possible value of the range

    Returns:
        None: if value is in range

    Raises:
        ValidationError: If `value` is lower or higher than bounds
    """
    if value not in range(lowbound, highbound + 1):
        raise ValidationError('{} is not within range {} to {} (inclusive)'
                              .format(value, lowbound, highbound))


within_white_range = partial(_within_range, lowbound=1, highbound=69)
"""fn: partially applied function to check the powerball white ball range"""

within_red_range = partial(_within_range, lowbound=1, highbound=26)
"""fn: partially applied function to check the powerball red ball range"""

