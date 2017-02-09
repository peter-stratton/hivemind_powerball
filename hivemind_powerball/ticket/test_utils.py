# ticket/test_utils.py
from django.test import TestCase

from . import utils


class TicketUtilityTest(TestCase):

    def test_group_by_popularity_returns_correct_groupings(self):
        data = [(1,5), (2, 5), (3, 4), (4, 4), (5, 4)]
        grouped = utils._group_by_popularity(data)
        self.assertEqual(2, len(grouped))

    def test_composite_ticket_returns_correct_tickets(self):
        data = [(1,5), (2,5), (3,4), (4,4), (5,4)]
        grouped = utils._group_by_popularity(data)
        ticket = utils._composite_ticket(grouped, 2)
        self.assertEqual([1,2], sorted(ticket))
        data = [(1,5), (2,5), (3,4), (4,4), (5,4)]
        grouped = utils._group_by_popularity(data)
        ticket = utils._composite_ticket(grouped, 3)
        self.assertIn(1, sorted(ticket))
        self.assertIn(2, sorted(ticket))
        data = [(1,5), (2,5), (3,4), (4,4), (5,4)]
        grouped = utils._group_by_popularity(data)
        ticket = utils._composite_ticket(grouped, 4)
        self.assertIn(1, sorted(ticket))
        self.assertIn(2, sorted(ticket))
        data = [(1,5), (2,5), (3,4), (4,4), (5,4)]
        grouped = utils._group_by_popularity(data)
        ticket = utils._composite_ticket(grouped, 5)
        self.assertIn(1, sorted(ticket))
        self.assertIn(2, sorted(ticket))

    def test_ball_query_raises_correct_error_when_bad_data_passed_in(self):
        self.assertRaises(TypeError, utils._ball_query_for, 'bad_input')
