# ticket/utils.py
import itertools
from random import randint

from django.db import connection


def _group_by_popularity(data):
    groups = []
    for k, g in itertools.groupby(data, lambda x: x[1]):
        groups.append(list(g))
    return groups


def _ball_query_for(color):
    """legal colors are `red` and `white`"""
    cursor = connection.cursor()
    cursor.execute("SELECT value, COUNT(value) FROM ticket_{}ball GROUP BY value ORDER BY 2 DESC".format(color))
    return cursor.fetchall()


def _composite_ticket(group_list, ticket_length):
    ticket = []
    while len(ticket) < ticket_length:
        for group in group_list:
            if len(ticket) == ticket_length:
                break
            while len(ticket) < ticket_length and len(group) > 0:
                ticket.append(group.pop(randint(0, len(group) - 1))[0])
    return ticket


def get_golden_ticket():
    red_results = _ball_query_for('red')
    white_results = _ball_query_for('white')
    if not len(red_results) > 0 and not len(white_results) > 0:
        return None
    red_groups = _group_by_popularity(red_results)
    white_groups = _group_by_popularity(white_results)
    return _composite_ticket(white_groups, 5), _composite_ticket(red_groups, 1)



