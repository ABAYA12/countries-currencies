# Return the sqaure of a number
y = {x: x**2 for x in range(100000000000000000000)}

while True:
    try:
        guest = int(input('Enter a number and return its square: '))
        if guest in y:
            print(f"{guest} = {y[guest]}")

            break
    except (ValueError):
        print("Please number can not be a character")
