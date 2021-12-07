def FromBinaryToDecimal(DecimalNumber1, DecimalNumber2):
    BinaryList1 = [0,0,0,0,0,0,0,0]
    BinaryList2 = [0,0,0,0,0,0,0,0]
    for i in range(len(BinaryList1) - 1, -1, -1):
        if DecimalNumber1 != 0: 
            Remainder1 = DecimalNumber1 % 2
            BinaryList1[i]= Remainder1
            DecimalNumber1  = DecimalNumber1//2
           
        if DecimalNumber2 != 0:
            Remainder2 = DecimalNumber2 % 2
            BinaryList2[i]= Remainder2
            DecimalNumber2= DecimalNumber2//2

    return BinaryList1, BinaryList2
