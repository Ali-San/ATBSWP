'''
From the book "Automate the Boring Stuff with Python"

https://automatetheboringstuff.com/2e/chapter8/

Chapter 8. Input Validation

Sandwich Maker
Write a program that asks users for their sandwich preferences.
'''
import pyinputplus as pyip
import time


price_list = {'Bread': 0.5, 'Protein': 1.2, 'Cheese': 1.5, 'Veggies': '1 / 1.4 / 1.8', 'Sauce': 0.25}


def build_sandwich(quantity):
	''' int -> list
	
	Ask the user for input to make the order.	Return a list with quantity sandwiches in it, where each sandwich is also a list.
	
	>>> order = build_sandwich(2)
	>>> print(order)
	order = [['White', 'Beef', 'Cheddar', ['Lettuce'], 'Mayo'], ['Rye', 'Ham', 'Havarti', ['Cucumber slices', 'Pickles', 'Mushrooms'], 'BBQ']]
	'''
	order = []
	
	for sandwich in range(quantity):
		this_sandwich = []
		bread = pyip.inputMenu(['White', 'Wheat', 'Rye', 'Sourdough', 'Onion', 'Garlic', 'With Seeds'], numbered= True, prompt="What type of bread would you like for this sandwich?\n")
		this_sandwich.append(bread)
		protein = pyip.inputMenu(['Beef', 'Chicken', 'Turkey', 'Ham', 'Tofu', 'Fried Egg', 'Chopped Boiled Egg', 'No protein'], numbered= True, prompt="What type of protein would you like?\n")
		this_sandwich.append(protein)
		cheese_1 = pyip.inputYesNo(prompt="Would you like cheese with it? (y/n)\n")
		if cheese_1 == 'yes':
			cheese_2 = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella', 'Havarti', 'Parmesan', 'Feta crumbles', 'Roquefort', 'Port Salut', 'Brie', 'Camembert'], numbered=True, prompt="What type of cheese would you like to add?\n")
			this_sandwich.append(cheese_2)
		else:
			this_sandwich.append("No")
		veggies_1 = pyip.inputYesNo(prompt="Would you like some veggies with your sandwich? (y/n)\n")
		if veggies_1 == 'yes':
			num_veggie = pyip.inputChoice(['1', '2', '3'], prompt="How many veggies would you like to add? (1, 2 or 3)\n")
			veggies = []
			for num in range(int(num_veggie)):
				veggies_2 = pyip.inputMenu(['Lettuce', 'Tomato slices', 'Cucumber slices', 'Pickles', 'Mushrooms', 'Green Olives', 'Black Olives', 'Sauted Eggplant', 'Bell Peppers', 'Chili Peppers', 'Onion slices', 'Shredded Carrots'], numbered=True, prompt="What veggie would you like to add?\n")
				veggies.append(veggies_2)
			this_sandwich.append(veggies)
		else:
			this_sandwich.append(["No veggies"])
		sauce = pyip.inputMenu(['Mayo', 'Dijon Mustard', 'Ketchup', 'Ranch', 'Tzatziki', 'Teriyaki', 'BBQ'], numbered=True, prompt="And finally, what sauce would you like to add?\n")
		this_sandwich.append(sauce)
		print('\n')
	
		order.append(this_sandwich)
	
	return order


def order_total(order):
	'''
	list -> tuple (list of ints, int)
	
	Return a tuple containing a list with the individual prices for each sandwich and the order's total price.
	
	>>>total = order_total(order)
	>>>print(total)
	([4.45, 5.25], 9.7)
	'''
	order_prices = []
	for sandwich in order:
		sandwich_price = 0.75
		if sandwich[1] == 'No protein':
			pass
		else:
			sandwich_price += 1.2
		if sandwich[2] == 'No':
			pass
		else:
			sandwich_price += 1.5
		if sandwich[3] == ['No veggies']:
			pass
		elif len(sandwich[3]) == 1:
			sandwich_price += 1
		elif len(sandwich[3]) == 2:
			sandwich_price += 1.4
		elif len(sandwich[3]) == 3:
			sandwich_price += 1.8
		order_prices.append(sandwich_price)
	
	order_total = sum(order_prices)
	
	return order_prices, order_total




### program start:
print("\tWelcome to The Sandwich Shop!\n\tIf you could use a sandwich,\n\tyou are in the right place!\n\n\tAll our sandwiches are big enough\n\tto make a hungry grown up happy,\n\tso keep that in mind\n\twhen you make your choices!\n\n")
time.sleep(1)

print("Here are the prices for the ingredients you may choose\nto build the best sandwiches:\n")

for item, price in price_list.items():
	print("*  " + item + ": " + str(price))

print("\n*  The first veggie costs $1.\n   You may add 2 more for an extra $0.40 each.\n")
time.sleep(1)

# ask how many sandwiches
quantity = pyip.inputInt(min=1, max=10, prompt="I will guide you through all our options. But first, how many sandwiches would you like to order?\n")
print("OK, let's start!\n")

# build the order
order = build_sandwich(quantity)

# calculate prices
total = order_total(order)
time.sleep(1)

# display order with prices
print("\nHere's your order")
sandwich_index = 0
for sandwich in order:
	veggie_1 = sandwich[3][0]
	try:
		veggie_2 = sandwich[3][1]
	except:
		IndexError
		veggie_2 = ""
	try:
		veggie_3 = sandwich[3][2]
	except:
		IndexError
		veggie_3 = ""

	veggies = veggie_1 + ' - ' + veggie_2 + ' - ' + veggie_3
	
	print("• 1 sandwich with\n\t• {} bread\n\t• {}\n\t• {} cheese\n\t• {}\n\t• {} sauce.\n\t.....$ {}".format(sandwich[0], sandwich[1], sandwich[2], veggies, sandwich[4], round(total[0][sandwich_index], 2)))
	sandwich_index += 1

print("\nYour total is $", round(total[1], 2))