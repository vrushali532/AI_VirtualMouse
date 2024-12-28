import calendar as cal

def show_month_calendar():
        month = int(input("Enter the month (1-12): "))
        year = int(input("Enter the year: "))
        print(f"\nCalendar for {cal.month_name[month]} {year}:")
        print(cal.month(year, month))
   


    

