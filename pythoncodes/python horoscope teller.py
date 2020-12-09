print("welcome to the Python Horoscope Generator!")
print()
month = input("Enter number the Month You Wre Born in (ex. 11 for november)")
print()
day = input("Enter the day you were born on (ex. 8,16,20)")

print()
day = int(day)
month = int(month)

if (month == 3 and day >= 21 or month == 4 and day <= 20):
    sign = "Aries"
elif (month == 4 and day >= 21 or month == 5 and day <= 20):
    sign = "Taurus"
elif (month == 5 and day >= 21 or month == 6 and day <= 20):
    sign = "Gemini"
elif (month == 6 and day >= 21 or month == 7 and day <= 22):
    sign = "Cancer"
elif (month == 7 and day >= 23 or month == 8 and day <= 22):
    sign = "Leo"
elif (month == 8 and day >= 23 or month == 9 and day <= 22):
    sign = "Virgo"
elif (month == 9 and day >= 23 or month == 10 and day <= 22):
    sign = "Libra"
elif (month == 10 and day >= 23 or month == 11 and day <= 22):
    sign = "Scorpio"
elif (month == 11 and day >= 23 or month == 12 and day <= 21):
    sign = "Sagittarius"
elif (month == 12 and day >= 21 or month == 1 and day <= 19):
    sign = "Capricorn"
elif (month == 1 and day >= 20 or month == 2 and day <= 19):
    sign = "Aquarius"
elif (month == 2 and day >= 20 or month == 3 and day <= 20):
    sign = "Pices"
else:
    print("error, did not find your sign. Month is " + str(month) + "Day is " + str(day)) 
print("your sign is " + sign) 
