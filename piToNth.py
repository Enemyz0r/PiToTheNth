import math

def PiToNth(integer):
    print(round(math.pi, integer))

integer=int(input("To how many decimals do you wish to display pi? "))
PiToNth(integer)
