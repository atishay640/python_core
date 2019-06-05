'''
Datetime
'''

import datetime


# get current date and time

datetime_obj = datetime.datetime.now()
print(datetime_obj)
print('------------------------------------------------')
# inside date time

print(dir(datetime))
print('------------------------------------------------')

# datetime.date class

date_obj = datetime.date(2019,1,2)
print(date_obj)
print('------------------------------------------------')
# current date
print(datetime.date.today())

print('------------------------------------------------')
# time object

from datetime import time

tm = time()
print(tm)
print('------------------------------------------------')

tm = time(12,36,15)
print(tm)
print('------------------------------------------------')

tm = time(12,36,15,445452)
print(tm)
print('------------------------------------------------')


# datetime.datetime

current_date_time = datetime.datetime(2019,1,2,12,36,15,445452)
print(current_date_time)
print('------------------------------------------------')

# Difference between two dates.

date1 = datetime.date.today()
date2 = datetime.date(1995,10,7)
my_age_in_days = date1 - date2

print(my_age_in_days)
print('------------------------------------------------')

# Difference between two times.

time1 = datetime.timedelta(weeks=2,days=5,hours=1,seconds=3)
time2 = datetime.timedelta(weeks=3,days=6,hours=1,seconds=3)
time_diff = time2 - time1
print(time_diff)


