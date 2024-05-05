customer_name = input("what is the customer's name?: ")

goods = []
quantities = []
total_price = []
total = []
total_amount = 0
count = 0
while True:
	goods_purchased = input("What did user buy ?")
	goods.append(goods_purchased)

	quantity = int(input("how many pieces ? "))
	quantities.append(quantity)

	price_per_unit = int(input("How much per unit ? "))
	total_amount += price_per_unit * quantity

	total_price.append(price_per_unit)

	decision_made = input("Add more items ?(yes / no): ")
	total.append(quantity * price_per_unit)
	if decision_made.lower() != "yes":
		break

		

#System.out.print(" ")
	#String blan 
name_of_cashier = input("What is your name: ?") 
customer_discount = int(input("How much discount will He/She get ? "))
print(" ")
discount = total_amount *customer_discount / 100
vat = total_amount * 17.50 / 100
bill = total_amount - discount + vat




print("\n\nSemicolon stores\nMain  Branch\nLocation: 312, HERBERT MACULAY WAY, SABO YABA, LAGOS.\nTel : 03293828343\nDate : 18 - Dec - 22 8 : 48 : 11 pm")
print("\nCashier  : " + name_of_cashier)
print("\nCustomer Name  : " + customer_name)
print("\n\n============================================")

print("\n" + "\tITEM\tQTY\tPRICE\tTOTAL(NGN)\n\n----------------------------------------------------------------------")
for i in range(len(goods)):
	print(f"\t{goods[i]}\t{quantities[i]}\t{total_price[i]}\t{total[i]}");

print("-------------------------------------------------------------------------------")
print(f"\n\t\t\tSub Total :  {total_amount}")
print(f"\n\t\t\tDiscount :  { discount}")
print(f"\n\t\t\tVat @ 17.50% : {vat}")
print("\n-----------------------------------------------------------------------------")
print(f"\n\t\t\tBill Total : {bill}")
print("\n==========================================================")
print(f"\nThis Is Not An RECEIPT KINDLY Pay   {bill}")
print("\n" + "=====================================================")


customer_input = int(input("\n" + "How much did the customer give to you? "))
print("\n\n\n\n\n\n\n ")



balance = customer_input - bill
print("SEMICOLON STORES\nMAIN BRANCH\nLOCATION : 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\nTEL : 18-Dec-22 8 : 57 : 31 pm\nCashier : " + name_of_cashier +"\nCustomer Name : " + customer_name)
print("\n\n===========================================================================")

print("\n\tITEM\tQTY\tPRICE\tTOTAL(NGN)\n\n-----------------------------------------------------------------------------------------")
for i in range(len(goods)):
	print(f"\t{goods[i]}\t{quantities[i]}\t{total_price[i]}\t{total[i]}");

print("------------------------------------------------------------------------------------------------------")
print(f"\n\t\t\tSub Total :  {total_amount}")
print(f"\n\t\t\tDiscount : {discount}")
print(f"\n\t\t\tVat @ 17.50% : {vat}")
print("\n-----------------------------------------------------------------------------------------------------")
print(f"\n\t\t\tBill Total : {bill}")
print(f"\n\t\t\tAmount Paid : {customer_input}")
print(f"\n\t\t\tBalance : {balance}")
print("\n================================================================================")
print("\nThanks You For Your Patronage")
print("\n================================================================================")