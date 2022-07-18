"""
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""
from datetime import *

# Get Today's Date
today = date.today()
print("Today: " + today.strftime('%d %b %Y'))

# Find out the date of next summer:
thisYear = today.year
xmas = date(thisYear, 12, 25)  # Dec 25

if today < xmas:
    print("Next Christmas: " + xmas.strftime('%d, %b %Y'))
    # Calculate the number of days till Christmas
    delta = (xmas - today).days
    print(str(delta) + " days left until Christmas!")
elif today == xmas:
    print("Today is Chirstmas Day!")
else:
    # We've passed this year's Christmas, we will need to wait for next year!
    nextXmas = date(thisYear + 1, 12, 25)
    print("Next Christmas: " + nextXmas.strftime('%d, %b %Y'))
    delta = (nextXmas - today).days
