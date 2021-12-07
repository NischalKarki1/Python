def validation():
    toContinue = True
    while toContinue:
        try:
            a = int(input("**Enter the first decimal number : "))
            print("\n")
            b = int(input("**Enter the second decimal number: "))
            if (0 <= a <= 255) and (0 <= b <= 255):
                sumOfNumbers = a + b
                if sumOfNumbers > 255:
                    print("please enter numbers whose sum will be less than or equal to 255")
                    toContinue = True

                else:
                    toContinue = False
                    return a, b
            else:
                print("Invalid decimal numbers, the numbers should be greater than 0 and less than 255")
                toContinue = True
        except ValueError:
            print("Please enter valid decimal values!")

