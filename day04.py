from datetime import date, timedelta, datetime


start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)

# The assignment, completed using the given dates above
def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    return str(start_100days + timedelta(days=+100)) 

def get_days_between_pb_start_first_joint_pycon(pybites_founded, pycon_date):
    """Return the int number of days"""
    end_date = pycon_date - pybites_founded
    return int(end_date.days)

# Additional stuff that interested me

def ending_date():
    day_number = int(input("Today is day what of your 100 days of Python? "))
    print(f"Your end date will be {datetime.now() + timedelta(100-day_number)}")

if __name__ == "__main__":
    print(get_hundred_days_end_date())
    print(get_days_between_pb_start_first_joint_pycon(pybites_founded, pycon_date))
    ending_date()