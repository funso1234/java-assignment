import random

array = []

for  arrays in range(10):

    numbers = random.randint(1, 50)

    array.append(numbers)

print(array)







my_list = [2, 4, 8, 8, 3, 7, 10]

count = 0

for element in my_list:

     count += 1

print(count)



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_Even = sum(my_list)

for i in range(len(my_list)):

               if i % 2 == 0:

                    print(sum_Even)




my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

sum_Odd = sum(my_list)

for i in range(len(my_list)):

     if i % 2 != 0:

          print(sum_Odd)





my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

product = 1

for i in my_list[2::3]:

     product *= i

print(product)






my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

average = sum(my_list) / len(my_list)

print(average)




my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

largest_Number = max(my_list)

print(largest_Number)



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

smallest_Number = min(my_list)

print(smallest_Number)