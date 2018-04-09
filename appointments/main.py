from meeting_calendar import Calendar
from file_input_reader import FileInputReader

if __name__ == "__main__":
    print("Please enter the path to input file...")
    file_input_reader = FileInputReader(input())
    office_hours, booking_requests = file_input_reader.read_booking_requests()
    calendar1 = Calendar(office_hours)
    calendar1.process_booking_requests(booking_requests)
    calendar1.display_meetings()
