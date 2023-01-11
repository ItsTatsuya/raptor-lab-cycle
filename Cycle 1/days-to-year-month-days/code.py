in_days = int(input("Enter number of days: "))
years = in_days//365
months = (in_days-years*365) // 30
days = (in_days-years*365-months*30)

print("Years=", years)
print("Months=", months)
print("Days=", days)
