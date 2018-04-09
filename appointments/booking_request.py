from datetime import datetime


class BookingRequest:
    def __init__(self, booking_request_date, booking_request_time, booking_request_employee_id,
                 meeting_date, meeting_start_time, meeting_duration):
        self.booking_request_date_time = datetime.strptime(booking_request_date + ' ' +
                                                           booking_request_time, '%Y-%m-%d %H:%M:%S')
        self.booking_request_employee_id = booking_request_employee_id
        self.meeting_start_date_time = datetime.strptime(meeting_date + ' ' + meeting_start_time,
                                                         '%Y-%m-%d %H:%M')
        self.meeting_duration = int(meeting_duration)

