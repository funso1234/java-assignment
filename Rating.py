numberofyears = int(input('Enter the number of years'))

principal = int(input('Enter the amount orignal invested'))

Numberofamonthinayear = 12

rate = 0.07/Numberofamonthinayear

baserate = 1 + rate

base = baserate ** numberofyears

amountofdeposit = principal * base

print('The amount of deposit is', amountofdeposit) 