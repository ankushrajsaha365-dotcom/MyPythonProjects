class DayError(Exception):
    pass

class MonthError(Exception):
    pass

class YearError(Exception):
    pass


try:
    print("Format: dd-mm-yyyy")
    dob_input = input("Enter your D.O.B.: ")

    parts = dob_input.split('-')

    if len(parts) != 3:
        raise ValueError("Invalid format! Use dd-mm-yyyy")

    day, month, year = map(int, parts)

    if year < 1900 or year > 2025:
        raise YearError("Year out of acceptable range")

    if month < 1 or month > 12:
        raise MonthError("Month must be between 1 and 12")

    # Leap year check
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if month in [1,3,5,7,8,10,12]:
        if day < 1 or day > 31:
            raise DayError("Invalid day for this month")

    elif month in [4,6,9,11]:
        if day < 1 or day > 30:
            raise DayError("Invalid day for this month")

    elif month == 2:
        if is_leap:
            if day < 1 or day > 29:
                raise DayError("Invalid day for February (leap year)")
        else:
            if day < 1 or day > 28:
                raise DayError("Invalid day for February")

except ValueError as e:
    print("Input Error:", e)

except (DayError, MonthError, YearError) as e:
    print("Validation Error:", e)

else:
    print(f"Valid DOB: {day}-{month}-{year}")