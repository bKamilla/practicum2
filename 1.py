#practicum2

summa = int(input())
silverq = 96
goldenq = 96 / 16
silverprice = 48
silversum = 48 * silverq
goldensum = summa - silversum
goldenprice = goldensum / goldenq
print(round(goldenprice))