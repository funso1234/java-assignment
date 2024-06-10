
#a = 0

#b = 1

#for numbers in range (0, 11):
 #   print(a, end=" ")
  #  a, b = b, a + b



count = 0
a = 0

b = 1
next_number = b

while count <= 0:
    print(next_number, end=" ")
    a, b = b, next_number
    next_number = a + b
    #print(next_number, end=" ")
    count += 1



 