score = int(input('Enter number: '))
largest = score;
for number in range(1, 10):
       score = int(input('Enter number: '))
       if score > largest:
          largest = score
print("The largest number is: ", largest)