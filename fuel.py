while True:
    try:
        # Prompt user for fuel fraction
        fuel_fraction = input("Enter fuel fraction (X/Y): ")

        # Split fraction into X and Y
        x, y = fuel_fraction.split("/")

        # Convert X and Y to integers
        x = int(x)
        y = int(y)

        # Check for invalid inputs
        if x < 0 or y < 0 or x > y or y == 0:
            raise ValueError

        # Calculate fuel percentage
        percent = x / y * 100

        # Check if tank is empty or full
        if percent <= 1:
            print("E")

        elif percent >= 99:
            print("F")

        else:
            print(round(percent))

        break
    except ValueError:
        print("Invalid input, enter a valid fraction (X/Y).")

    except ZeroDivisionError:
        print("Invalid input.Denominator can't be zero.")
