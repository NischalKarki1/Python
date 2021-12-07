#for and gate
def andGate(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

# for or gate
def orGate(a, b):
    if a == 0 and b == 0:
        return 0
    else:
        return 1

#for xor gate
def xorGate(a, b):
    if (a == 1 and b == 1) or (a == 0 and b == 0):
        return 0
    else:
        return 1
