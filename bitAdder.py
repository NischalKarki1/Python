import gates as g
def bitAdder(l2, l3):
    sumOfBinary = [0] * 8
    carryIn = 0
    for i in range(len(l2)-1, -1, -1):
        #for sum 
        sum1 = g.xorGate(l2[i], l3[i])
        sum2 = g.xorGate(sum1, carryIn)
        sumOfBinary[i] = sum2

        #for carry over    
        fco = g.andGate(l2[i], l3[i])
        fco2 = g.xorGate(l2[i],l3[i])
        fco3 = g.andGate(fco2, carryIn)
        finalCo = g.orGate(fco3, fco)
        carryIn = finalCo
    return sumOfBinary

