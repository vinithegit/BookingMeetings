from unittest import TestCase

from appointments.booking_request import BookingRequest
from appointments.meeting_calendar import Calendar
from appointments.meeting import Meeting
from appointments.office_hours import OfficeHours


class TestCalendar(TestCase):
    def test_process_booking_requests(self):
        office_hours = OfficeHours("0900", "1730")
        calendar = Calendar(office_hours)
        booking_request1 = BookingRequest("2015-08-17", "10:17:06", "EMP001",
                                          "2015-08-21", "09:00", "2")
        booking_request2 = BookingRequest("2015-08-16", "12:34:56", "EMP002",
                                          "2015-08-21", "09:00", "2")
        booking_request3 = BookingRequest("2015-08-16", "09:28:23", "EMP003",
                                          "2015-08-22", "14:00", "2")
        booking_request4 = BookingRequest("2015-08-17", "11:23:45", "EMP004",
                                          "2015-08-22", "16:00", "1")
        booking_request5 = BookingRequest("2015-08-15", "17:29:12", "EMP005",
                                          "2015-08-21", "16:00", "3")

        booking_requests = [booking_request1, booking_request2, booking_request3, booking_request4, booking_request5]
        meeting1 = Meeting(booking_request2)
        meeting2 = Meeting(booking_request3)
        meeting3 = Meeting(booking_request4)
        meetings = calendar.process_booking_requests(booking_requests)
        self.assertEqual(3, len(meetings))
        self.assertTrue(meeting1 in meetings)
        self.assertTrue(meeting2 in meetings)
        self.assertTrue(meeting3 in meetings)

    def test_display_meetings(self):
        office_hours = OfficeHours("0900", "1730")
        calendar = Calendar(office_hours)
        booking_request1 = BookingRequest("2015-08-17", "10:17:06", "EMP001",
                                          "2015-08-21", "09:00", "2")
        booking_request2 = BookingRequest("2015-08-16", "12:34:56", "EMP002",
                                          "2015-08-21", "09:00", "2")
        booking_request3 = BookingRequest("2015-08-16", "09:28:23", "EMP003",
                                          "2015-08-22", "14:00", "2")
        booking_request4 = BookingRequest("2015-08-17", "11:23:45", "EMP004",
                                          "2015-08-22", "16:00", "1")
        booking_request5 = BookingRequest("2015-08-15", "17:29:12", "EMP005",
                                          "2015-08-21", "16:00", "3")

        booking_requests = [booking_request1, booking_request2, booking_request3, booking_request4, booking_request5]
        calendar.process_booking_requests(booking_requests)
        calendar.display_meetings("calendar_output_file")
        expectation = "2015-08-21\n" \
                      "09:00 11:00 EMP002\n" \
                      "2015-08-22\n" \
                      "14:00 16:00 EMP003\n" \
                      "16:00 17:00 EMP004\n"
        with open("calendar_output_file",'r') as out_file:
            self.assertEqual(expectation, out_file.read())



