# Days left until Summer
from datetime import *

# Get Today's Date
today = date.today()
print("Today: " + today.strftime('%A %d, %b %Y'))

dob_str = input("What is your Date of Birth? dd/mm/yyyy ")

# Convert user input into a date
dob_data = dob_str.split("/")
dobDay = int(dob_data[0])
dobMonth = int(dob_data[1])
dobYear = int(dob_data[2])
dob = date(dobYear, dobMonth, dobDay)

# Calculate number of days lived
numberOfDays = (today - dob).days

# Convert this into whole years to display the age
age = numberOfDays // 365

# Calculating the number of candles
i = str(age)
num = int(i[1:2])
i = "i"*num

# Calculating the number of days until next birthday
thisYear = today.year

nextBirthday = date(thisYear, dobMonth, dobDay)
if today < nextBirthday:
    gap = (nextBirthday - today).days
    print("Your birhday is in " + str(gap) + " days.")
elif today == nextBirthday:
    print(f'''Today is your birthday!
       ___{i}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
  ''')
else:
    nextBirthday = date(thisYear+1, dobMonth, dobDay)
    gap = (nextBirthday - today).days
    print("Your birthday is in " + str(gap) + " days.")
