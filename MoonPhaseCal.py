from datetime import datetime

cynodic_phase_time = 29.530588

# calculates the julian date based off of a date provided. The julian date is 
# the number of days since Jan. 1, 4713 bc

def calculate_julian_date(date):
    month = date.month + 12 if date.month == 1 or date.month == 2 else date.month
    year = date.year - 1 if date.month == 1 or date.month == 2 else date.year
    day = date.day + (date.hour / 24) + (date.minute / 1440) + (date.second / 86400)

    JD = (365.25 * year) + (30.6001 * (month + 1)) + day + 1720981.5

    if year < 1582 or (year == 1582 and (month < 10 or (month == 10 and day <= 4))):
        pass
    else:
        gregorian_switch = year // 100
        JD -= gregorian_switch
        JD += gregorian_switch // 4
        JD += 38

    return JD

# calculates T or the time in centuries since the epoch J2000.0

def calculate_julian_centuries(JD):
    return (JD - 2451545.0) / 36525


# calculates the mean longitude of the moon 

def calculate_mean_moon_longitude(T):
    L0 = 218.3164477
    L1 = 481267.88123421
    L2 = -0.0015786
    L3 = 1 / 538841

    return (L0 + (L1 * T) + (L2 * (T ** 2)) + (L3 * (T ** 3))) % 360


# calculates the mean moon elongation

def calculate_mean_moon_elongation(T):
    D0 = 297.8501921
    D1 = 445267.11140440

    return (D0 + D1 * T) % 360

# calculates the mean moon anomaly

def calculate_mean_moon_anomaly(T):
    pass

# calculates the moon's argument of latitude

def calculate_moon_argument_latitude(T):
    pass


# calculates the mean sun anomaly

def calculate_mean_sun_anomaly(T):
    pass


# returns true if value is a string, false if it is not

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# prompts user for integer input

def get_integer_input(prompt):
    while True:
        value = input(prompt)
        if is_integer(value):
            return int(value)
        else:
            print("Invalid input. Please enter a valid integer.")


# gets the date info from the user for the calculation of the moon phase

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

    datetime_from_user = get_date_input()
    JD = calculate_julian_date(datetime_from_user)

    T = calculate_julian_centuries(JD)

    moon_mean_longitude = calculate_mean_moon_longitude(T)
    moon_mean_elongation = calculate_mean_moon_elongation(T)

    print(moon_mean_longitude)
    print(moon_mean_elongation)



if __name__ == "__main__":
    main()