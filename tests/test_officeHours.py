from datetime import time
from unittest import TestCase

from appointments.office_hours import OfficeHours


class TestOfficeHours(TestCase):
    def test_is_within_office_hours(self):
        office_hours = OfficeHours("0900", "1730")
        is_within = office_hours.is_within_office_hours(time(hour=10, minute=30))
        self.assertTrue(is_within)
        is_within = office_hours.is_within_office_hours(time(hour=18, minute=30))
        self.assertFalse(is_within)
        is_within = office_hours.is_within_office_hours(time(hour=17, minute=30))
        self.assertTrue(is_within)