year = int(input("Enter any year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year," Is leap year")
else:
    print(year," Is not leap year")