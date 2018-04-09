import os

from booking_request import BookingRequest
from errors import InvalidFileContentError
from office_hours import OfficeHours


class FileInputReader:
    def __init__(self, input_file_name):
        self._input_file_name = input_file_name

    def read_booking_requests(self):
        if not os.path.isfile(self._input_file_name):
            raise FileNotFoundError("Input file not found!!")
        with open(self._input_file_name, 'r') as input_file:
            file_contents = input_file.read().splitlines()
            try:
                office_hours_begin, office_hours_end = tuple(file_contents[0].split())
                office_hours = OfficeHours(office_hours_begin, office_hours_end)
                booking_requests = []
                booking_request_date, booking_request_time, booking_request_employee_id, meeting_date, \
                    meeting_start_time, meeting_duration = None, None, None, None, None, None

                for index in range(1, len(file_contents)):
                    line_as_tuple = tuple(file_contents[index].split())
                    if index % 2 ==1:
                        booking_request_date, booking_request_time, booking_request_employee_id = line_as_tuple
                    else:
                        meeting_date, meeting_start_time, meeting_duration = line_as_tuple
                        booking_request = BookingRequest(booking_request_date, booking_request_time, booking_request_employee_id,
                                                         meeting_date, meeting_start_time, meeting_duration)
                        booking_requests.append(booking_request)
                return office_hours, booking_requests

            except:
                raise InvalidFileContentError("File input incorrect!!")










