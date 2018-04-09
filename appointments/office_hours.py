from datetime import datetime


class OfficeHours:
    def __init__(self,office_hours_begin, office_hours_end):
        self.office_hours_begin = datetime.time(datetime.strptime(office_hours_begin, '%H%M'))
        self.office_hours_end = datetime.time(datetime.strptime(office_hours_end, '%H%M'))

    def is_within_office_hours(self, time_to_check):
        if time_to_check >= self.office_hours_begin and time_to_check <= self.office_hours_end:
            return True
        return False

