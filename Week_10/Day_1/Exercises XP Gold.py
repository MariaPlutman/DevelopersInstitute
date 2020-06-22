from datetime import *
import holidays

# Exercise 1
today = date.today()
print("Today: " + today.strftime('%A %d, %b %Y'))

# Exercise 2
dob_str = "01/01/2021"
dob_data = dob_str.split("/")
dobDay = int(dob_data[0])
dobMonth = int(dob_data[1])
dobYear = int(dob_data[2])
thisYear = today.year
next_January = date(thisYear, dobMonth, dobDay)
gap = (today-next_January).days
print("New year is in " + str(gap) + " days.")

# Exercise 3
il_holidays = holidays.Israel()
for date, name in holidays.Israel(years=2020).items():
    print(date, name)
