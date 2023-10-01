#beginning and intial presets
master_list = []
others = []
drinks = ["sprite", "root beer", "apple juice", "iced tea", "coffee"]
credit = 3.00
drink_menu = [2.99, 3.99, 0.99, 2.99, 1.99]
meal_menu = [2.49, 0.99, 1.99, 3.99]
foods = ["burger", "fries", "hot dog", "chicken salad"]


#functions
def meal_price(option):
	global credit
	for i, selection in enumerate(foods):
		if selection == option:
			if meal_menu[i] <= credit:
				print("Your food price is: " + str(meal_menu[i]))
				master_list.append(option)
				master_list.append(str(meal_menu[i]))
				credit -= meal_menu[i]
				print("Your remaining balance is: " + str(round(credit, 3)))

			else:
				alternates(credit)


#drink function
def drink_price(request):
	global credit
	for i, selection in enumerate(drinks):
		if selection == request:
			if drink_menu[i] < credit:
				print("Your drink price is: " + str(drink_menu[i]))
				master_list.append(request)
				master_list.append(str(drink_menu[i]))
				credit -= drink_menu[i]
				print("Your remaining balance is: " + str(round(credit, 3)))
			else:
				print("Not enough for a drink. ")
				alternates(credit)


#what are the alternates?
def alternates(credit):
	for i in range(len(meal_menu)):
		if credit > meal_menu[i]:
			others.append(foods[i])
	for j in range(len(drink_menu)):
		if credit > drink_menu[j]:
			others.append(drinks[j])
	if (others == []):
		print("You don't have enough for anymore items")
		return
	print("You don't have enough for this item, maybe try \n")
	print(" or ".join(others))
	retry = input("")
	meal_price(retry)
	drink_price(retry)


#start of program
credit = input("How much money do you have? (nearest whole #) ")
credit = (int)(credit)
print("Welcome to Zuro's Food Bar! You have $" + str(int(credit)) + " avaliable")
decision1 = input(" Would you like a drink? ")
if (decision1.lower() == "yes"):
	drink = input(
	 "Here is your drink options(Select 1): \n sprite, root beer, apple juice, iced tea, coffee \n"
	)
	drink_price(drink.lower())
	decision2 = input("Would you like a meal? ")
	if (decision2.lower() == "yes"):
		meal = input(
		 "Food options(Select 1): Burger, Fries, Hot Dog, Chicken Salad \n")
		print("Please wait as we are getting your price...")
		meal_price(meal.lower())

else:
	decision2 = input("Would you like a meal? ")
	if (decision2.lower() == "yes"):
		meal = input("Food options(Select 1): Burger, Fries, Hot Dog, Chicken Salad")
		print("Please wait as we are getting your price...")
		meal_price(meal)
	else:
		print("Okay, just come back when you want a meal. ")

#returning the total and order

print("Your order is: " + ", ".join(master_list))
