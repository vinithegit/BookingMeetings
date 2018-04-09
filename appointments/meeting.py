from datetime import datetime, timedelta


class Meeting:
    def __init__(self, booking_request):
        self.meeting_date = datetime.date(booking_request.meeting_start_date_time)
        self.employee_id = booking_request.booking_request_employee_id
        self.meeting_start_time = datetime.time(booking_request.meeting_start_date_time)
        self.meeting_end_time = datetime.time(booking_request.meeting_start_date_time +
                                              timedelta(hours=booking_request.meeting_duration))

    def __eq__(self, other):
        return (self.meeting_start_time == other.meeting_start_time and
                self.meeting_end_time == other.meeting_end_time and
                self.meeting_date == other.meeting_date and
                self.employee_id == other.employee_id)



