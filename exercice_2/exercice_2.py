def is_leap_year_v1(year):
    if year % 400 == 0:
        return True
    else:
        return False


def is_leap_year_v2(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        return True
    else:
        return False


def is_leap_year_v3(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def is_leap_year_v4(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
