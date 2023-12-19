#.Program to print a Calendar with total days, weeks and year for a particular date by taking input from the user.
import calendar
def print_calendar(year, month):
    # Print calendar for the specified year and month
    cal = calendar.monthcalendar(year, month)
    
    # Get total days and weeks
    total_days = sum(1 for week in cal for day in week if day != 0)
    total_weeks = len(cal)

    # Print calendar
    print("\nCalendar:")
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")

    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                print(f"{day:2d}", end=" ")
        print()

    print("\nTotal Days:", total_days)
    print("Total Weeks:", total_weeks)

# Get user input
year_input = int(input("Enter the year: "))
month_input = int(input("Enter the month (1-12): "))

# Print the calendar
print_calendar(year_input, month_input)

# Get user input for finding a particular day
day_input = int(input("\nEnter the day to find (1-31): "))

# Find the day
day_index = calendar.weekday(year_input, month_input, day_input)
day_name = calendar.day_name[day_index]

# Print the result
print(f"\nThe day on {day_input}/{month_input}/{year_input} is {day_name}.")
