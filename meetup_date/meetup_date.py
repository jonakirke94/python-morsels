import datetime
from enum import IntEnum


#  if we use IntEnum we don't have to call .value
class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=Weekday.THURSDAY):
    date_count = 1
    seen = 0

    if nth < 0:
        #  we can get the last day of the month by taking the next month and subtracting one
        #  should probably handle month overflow with modulus
        date_count = (datetime.date(year=year, month=month + 1, day=1) - datetime.timedelta(days=1)).day

    while True:
        the_date = datetime.date(year=year, month=month, day=date_count)

        if the_date.weekday() == weekday:
            seen = seen + (-1 if nth < 0 else 1)

            if seen == nth:
                return the_date

        date_count = date_count + (-1 if nth < 0 else 1)
