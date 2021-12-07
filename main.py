from validation import validation as val
from FromBinaryToDecimal import FromBinaryToDecimal as b
from bitAdder import bitAdder as bit
import greetings as g

UserName = g.Start()
print("\n")
continueLoop = True
while continueLoop:
    Num1, Num2 = val()
    BinaryList1, BinaryList2 = b(Num1, Num2)
    sumOfBinary = bit(BinaryList1, BinaryList2)
    print("\n")
    print(f"!!!The conversion of {Num1} to will be: {tuple(BinaryList1)}!!!")
    print("\n")
    print(f"!!!The conversion of {Num2} to binary will be: {tuple(BinaryList2)}!!!")
    print("\n")
    print(f"!!!Therefore, the sum of {tuple(BinaryList1)} and {tuple(BinaryList2)} will be: {tuple(sumOfBinary)}!!!")
    print("\n")

    continuation = input("Type (yes :) if you want to continue and no :( if you want to exit: ")
    if continuation == "no":
        print("\n")
        g.End(UserName)
        break
    elif continuation == "yes":
        continue
    else:
        print("!!!Something is incorrect. Please type (yes/no)!!!")
        continue
