calculation_to_units = 24
name_of_unit = "hours"


def days_to_units():
    while True:
        try:
            days = int(input(f"Please enter number of days, you wan to convert into hours: \n"))
            if days > 0:
                print(f"\nHi there, {days} days have {days * calculation_to_units} {name_of_unit}.")
                print("Thank you for using our program!\n")
            else:
                print("You entered invalid number, please enter correct value.")
        except ValueError:
                print("You entered invalid character, please enter a number.")

days_to_units()
