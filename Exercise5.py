# Create a dictionary with month numbers as keys and the number of days as values
days_in_month = {
    1: 31,  # January
    2: 28,  # February (we will handle leap years separately)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Ask the user to input the month number
month = int(input("Enter the month number (1-12): "))

# Check if the month is valid
if 1 <= month <= 12:
    if month == 2:  # If the month is February, ask about leap year
        leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap_year == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        # For other months, just print the number of days from the dictionary
        print(f"{days_in_month[month]} days")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
