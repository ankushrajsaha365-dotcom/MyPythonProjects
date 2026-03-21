import calendar

class DateError(Exception):
    pass

try:
    print("Format: dd-mm-yyyy")
    dob_input = input("Enter your D.O.B.: ")

    parts = dob_input.split('-')
    if len(parts) != 3:
        raise ValueError("Invalid format! Use dd-mm-yyyy")

    day, month, year = map(int, parts)

    if year < 1900 or year > 2025:
        raise DateError("Year out of acceptable range")

    if month < 1 or month > 12:
        raise DateError("Invalid month")

    # Get number of days in that month
    _, max_days = calendar.monthrange(year, month)

    if day < 1 or day > max_days:
        raise DateError(f"Invalid day! This month has {max_days} days")

except ValueError as e:
    print("Input Error:", e)

except DateError as e:
    print("Validation Error:", e)

else:
    print(f"Valid DOB: {day}-{month}-{year}")