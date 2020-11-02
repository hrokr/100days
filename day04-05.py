from datetime import date, timedelta, datetime


start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)

# The assignments, completed using the given dates above


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    return str(start_100days + timedelta(days=+100))


def get_days_between_pb_start_first_joint_pycon(pybites_founded, pycon_date):
    """Return the int number of days"""
    end_date = pycon_date - pybites_founded
    return int(end_date.days)

# Rolling on ...


THIS_YEAR = 2018


def years_ago(date_string):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
    date_obj = datetime.strptime(date_string, "%d %b, %Y")
    return THIS_YEAR - date_obj.year


def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
       Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
       To enforce the use of datetime's strptime / strftime (over slicing)
       the tests check if a ValueError is raised for invalid day/month/year
       ranges (no need to code this, datetime does this out of the box)"""
    dto = datetime.strptime(date, "%d/%m/%Y")
    return dto.strftime("%m/%d/%Y")


# Additional stuff that interested me

def ending_date():
    day_number = int(input("Today is day what of your 100 days of Python? "))
    print(f"Your end date will be {datetime.now() + timedelta(100-day_number)}")


if __name__ == "__main__":
    print(get_hundred_days_end_date())
    print(get_days_between_pb_start_first_joint_pycon(pybites_founded, pycon_date))
    ending_date()
    print(years_ago("23 Mar, 2020"))
    print(convert_eu_to_us_date('11/03/2002'))
