import sys

from meeting import Meeting


class Calendar:
    def __init__(self, office_hours):
        self.office_hours = office_hours
        self._meetings_map = {}

    def process_booking_requests(self, booking_requests):
        booking_requests.sort(key=lambda x: x.booking_request_date_time)
        meetings_list = []
        for request in booking_requests:
            meeting = Meeting(request)
            #checking if meeting within office hours
            if not (self.office_hours.is_within_office_hours(meeting.meeting_start_time) and
                    self.office_hours.is_within_office_hours(meeting.meeting_end_time)):
                continue
            key = request.meeting_start_date_time

            # checking if meeting time is free
            if key in self._meetings_map:
                continue
            self._meetings_map[key] = meeting
            meetings_list.append(meeting)
        return meetings_list

    def display_meetings(self, output_file=None):
        if output_file is None:
            sys.stdout.write(self._formatted_calendar())
        else:
            with open(output_file,'w') as fp:
                fp.write(self._formatted_calendar())

    def _formatted_calendar(self):
        output_string = ""
        sorted_meetings = sorted(self._meetings_map.items())
        prev_date = None
        for start_date_time, meeting in sorted_meetings:
            if meeting.meeting_date != prev_date:
                output_string += str(meeting.meeting_date) + '\n'
                prev_date = meeting.meeting_date
            output_string += "{} {} {}\n".format(meeting.meeting_start_time.strftime("%H:%M"),
                                                 meeting.meeting_end_time.strftime("%H:%M"),
                                                 meeting.employee_id)
        return output_string

