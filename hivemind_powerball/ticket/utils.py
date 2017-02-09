# ticket/utils.py
"""Utility functions for working with tickets and ticket values"""
import itertools
from random import randint

from django.db import connection


def _group_by_popularity(data):
    """Given a sorted list of 22tuples where tuple[0] is a ticket number, and
    tuple[1] is the number of times it was selected by users, returns a new
    list of lists containing the tuples with tied tuple[1] values.  The sorting
    is expected to be by the tuple[1] value.

    Example:
        Given the following database table:

            | user   | value |
            |--------|-------|
            | Ally   | 11    |
            | Ben    | 22    |
            | Clara  | 33    |
            | Don    | 11    |
            | Erin   | 22    |
            | Frank  | 11    |
            | Gina   | 42    |
            | Hank   | 33    |

        `data` would look like this:

            `[(11,3), (22,2), (33,2), (42,1)]`

    Args:
        data (list[2tuple]): The sorted list of 2tuples

    Returns:
        List: of lists of grouped 2tuples.  ex:

            `[[(11,3)], [(22,2), (33,2)], [(42,1)]]`
    """
    groups = []
    for k, g in itertools.groupby(data, lambda x: x[1]):
        groups.append(list(g))
    return groups


def _ball_query_for(color):
    """Conducts a database query to retrieve the grouped and counted values.
    Normally we wouldn't want to drop down to raw SQL in a Django query.  In
    situations where the information we are interested in retrieving from the
    database isn't directly related to Models, it doesn't make sense to use the
    Django ORM.  However, care must be taken that this function is never called
    with any type of user supplied `color` data, as this would open the way for
    malicious SQL injection attacks.

    Args:
        color (str): either 'red' or 'white', anything else raises TypeError

    Returns:
        List: of `(value, count)` tuples

    Raises:
        TypeError: if a value other than 'red' or 'white' is passed in
    """
    if color.upper() not in ['RED', 'WHITE']:
        raise TypeError
    cursor = connection.cursor()
    cursor.execute("SELECT value, COUNT(value) FROM ticket_{}ball GROUP BY value ORDER BY 2 DESC".format(color))
    return cursor.fetchall()


def _composite_ticket(group_list, ticket_length):
    """Given a list of lists of grouped `(value, count)` 2tuples, generates
    a composite ticket representing the most popular ticket values entered in
    the system.  If there is a tie (multiple tuple groups with the same
    popularity count) it randomly pops tuples out of the group until the
    `ticket_length` is met, or it empties the group.  Rinse. Repeat.

    Args:
        group_list (list[list[(tuples)]]): a list of lists of 2tuples grouped by
            their popularity count stored at tuple[1]

    Examples:
        >>> grouped_input = [[(4, 29)],
        ...                  [(2, 26)],
        ...                  [(3, 22), (5, 22), (1, 22)],
        ...                  [(6, 16)],
        ...                  [(7, 12)],
        ...                  [(9, 8)],
        ...                  [(8, 7)],
        ...                  [(45, 1)]]

        >>> _composite_ticket(grouped_input, 1)
        [4]

        >>> _composite_ticket(grouped_input, 2)
        [4, 2]

        >>> _composite_ticket(grouped_input, 3)  # nondeterministic
        # possible results: [4, 2, 3] or [4, 2, 5] or [4, 2, 1]

    Returns:
        List: representing the composite ticket of most popular values
    """
    ticket = []
    while len(ticket) < ticket_length:
        for group in group_list:
            if len(ticket) == ticket_length:
                break  # stop if we've met the ticket_length
            while len(ticket) < ticket_length and len(group) > 0:
                # Pop values off the group randomly until
                # we run out or meet ticket_length.
                ticket.append(group.pop(randint(0, len(group) - 1))[0])
    return ticket


def get_golden_ticket():
    """Performs all the steps required to generate the composite ticket

    Returns:
        None: if the database is empty
        Tuple: where tuple[0] holds the white ball values and tuple[1] holds
            the red powerball value.
    """
    red_results = _ball_query_for('red')
    white_results = _ball_query_for('white')
    if not len(red_results) > 0 and not len(white_results) > 0:
        return None  # database is empty, so don't try grouping the results
    red_groups = _group_by_popularity(red_results)
    white_groups = _group_by_popularity(white_results)
    return _composite_ticket(white_groups, 5), _composite_ticket(red_groups, 1)



