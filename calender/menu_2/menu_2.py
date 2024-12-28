import calendar
def show_year_calendar():
    try:
        # Take user input for the year
        year = int(input("Enter the year: "))
        
        # Display the calendar for the specific year
        print(f"\nCalendar for the year {year}:")
        print(calendar.calendar(year))
    except ValueError:
        print("Invalid input, please enter a valid integer for year.")

