from datetime import datetime

cynodic_phase_time = 29.530588

def calculate_julian_date(date):
    month = date.month + 12 if date.month == 1 or date.month == 2 else date.month
    year = date.year - 1 if date.month == 1 or date.month == 2 else date.year
    day = date.day + (date.hour / 24) + (date.minute / 1440) + (date.second / 86400)

    JD = (365.25 * year) + (30.6001 * (month + 1)) + day + 1720981.5

    if year < 1582 or (year == 1582 and (month < 10 or (month == 10 and day <= 4))):
        pass
    else:
        gregorian_switch = int(year / 100)
        JD -= gregorian_switch
        JD += int(gregorian_switch / 4)
        JD += 38

    return JD

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def get_integer_input(prompt):
    while True:
        value = input(prompt)
        if is_integer(value):
            return int(value)
        else:
            print("Invalid input. Please enter a valid integer.")

def get_date_input():
    year = get_integer_input("Enter year: ")
    month = get_integer_input("Enter month: ")
    day = get_integer_input("Enter day: ")
    hour = get_integer_input("Enter hour of day: ")
    minute = get_integer_input("Enter minute of day: ")
    second = get_integer_input("Enter second of day: ")

    return datetime(year, month, day, hour, minute, second)

def main():
    print("Moon Phase Calculator\n")

    dt = get_date_input()
    print(calculate_julian_date(dt))


if __name__ == "__main__":
    main()