from datetime import datetime
from unittest import TestCase

from appointments.errors import InvalidFileContentError
from appointments.file_input_reader import FileInputReader


class TestFileInputReader(TestCase):
    def test_read_booking_requests_raises_file_not_found_error(self):
        file_input_reader = FileInputReader("non_existent_file")
        self.assertRaises(FileNotFoundError, file_input_reader.read_booking_requests)

    def test_read_booking_requests_raises_invalid_file_content_error(self):
        file_input_reader = FileInputReader("invalid_input_file")
        self.assertRaises(InvalidFileContentError, file_input_reader.read_booking_requests)

    def test_read_booking_requests_returns_officehours_and_bookingrequests(self):
        file_input_reader = FileInputReader("valid_input_file")
        office_hours, booking_requests = file_input_reader.read_booking_requests()
        self.assertEqual(9, office_hours.office_hours_begin.hour)
        self.assertEqual(0, office_hours.office_hours_begin.minute)
        self.assertEqual(17, office_hours.office_hours_end.hour)
        self.assertEqual(30, office_hours.office_hours_end.minute)
        self.assertEqual(5, len(booking_requests))
        self.assertEqual(datetime.strptime("2015-08-15 17:29:12", '%Y-%m-%d %H:%M:%S'), booking_requests[4].booking_request_date_time)
        self.assertEqual("EMP005", booking_requests[4].booking_request_employee_id)
        self.assertEqual(datetime.strptime("2015-08-21 16:00", '%Y-%m-%d %H:%M'), booking_requests[4].meeting_start_date_time)
        self.assertEqual(3, booking_requests[4].meeting_duration)



