"""
SETUP
- each bike model is its own class
- properties for each bike contained inside that class 
- print each model name
	[could've dumped model names into a list and just printed that out]
- create list of bike model names

BUDGET
- get customer's budget
- sort price of bikes (ascending)
- compare customer's budget to each bike price (descending)
- 

[LATER - if customer's budget > highest price bike, ask type of bike wanted ("def wants" written)]

CUSTOMER
- get customer's FIRST, LAST, ADDRESS (St, City, ST, Zip)
- budget
- list of models customer can afford
- bike selection
- remaining $$ from their budget

INVENTORY
- number of bikes before customer purchase
- number of each model after customer purchase
= = = = = = = = = = = = = = = = = = = = = = = = = = =

- create classes for each model bike with *.properties
	^ sort classes by price of model
		* Fail
	^ throw each model.price into a list and sort by .price
		* Fail - new list doesn't retain new sort order   							Q:   WHY NOT?
	^ throw each model: price into a dictionary and sort by price
		* 











= = = = = = = = = = = = = = = = = = = = = = = = = = =
- what is the outcome expected
	^ 6 bike models
	^ 20% margin over cost
	^ 3 customers
		> 1 has budget of $200
		> 1 has budget of $500
		> 1 has budget of $1,000
	^ print:
		> name of each customer
		> list of bikes each can afford
	^ print initial inventory for each bike
	^ print:
		> name of bike purchased (by each customer)
		> cost of each bike
		> $ left over from each budget
	^ print:
		> remaining inventory for each model bike
		> profit made from the 3 bike sales
= = = = = = = = = = = = = = = = = = = = = = = = = = =


MODELS		  NAMES.Y		WEIGHT	MFR-COST	INV		CUST-NAME	CUST-BUDG
- road		  windy-tough	26 lb	$700		15		? (raw_input)	? (raw_input)
- mountain    windy-high	30 lb	$900		12		?				?
- fixed gear  windy-breeze	22 lb	$600		3		?				?
- city		  windy-sleek	28 lb	$550		23		?				?
- country	  windy-day		34 lb	$400		16		?				?
- kids'		  windy-gust	24 lb	$150		5		?				?

"""

# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =		SECTION 01
# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =			setting classes; storing price markup 

markup = .20

		
# using Classes by Bike Model:

class Bike:

	# Define model abbreviations
	MODEL = {
		TO: "Windy Tough",
		HI: "Windy High",
		BR: "Windy Breeze",
		SL: "Windy Sleek",
		DA: "Windy Day",
		GU: "Windy Gust"
	}
	
	# Define model styles
	STYLE = {
		TOUGH: "Road",
		HIGH: "Mountain",
		BREEZE: "Fixed Gear",
		SLEEK: "City",
		DAY: "Country",
		GUST: "Kids"
	}

	# Define model weights
	WEIGHT = {
		TOUGH: 26,
		HIGH: 30,
		BREEZE: 22,
		SLEEK: 28,
		DAY: 34,
		GUST: 24
	}

	# Define cost to produce
	COST = {
		TOUGH: 700.00,
		HIGH: 900.00,
		BREEZE: 600.00,
		SLEEK: 550,
		DAY: 400,
		GUST: 150
	}

	# Define price to include markup
	PRICE = {
		TOUGH: 700.00 + (700.00 * markup),
		HIGH: 900.00 + (900.00 * markup),
		BREEZE: 600.00 + (600.00 * markup),
		SLEEK: 550 + (550.00 * markup),
		DAY: 400 + (400.00 * markup),
		GUST: 150 + (150.00 * markup)
	}

	# Define initial inventory for each model
	INVENTORY = {
		TOUGH: 15,
		HIGH: 12,
		BREEZE: 3,
		SLEEK: 23,
		DAY: 16,
		GUST: 5
	}
	
		
	def __init__(self, model, style, weight, cost, price, inventory):
		# Save the model, style, weight, cost, price & inventory
		self.model = model
		self.style = style
		self.weight = weight
		self.cost = cost
		self.price = price
		self.inventory = inventory
		
		
		
# print Bike(BRIEF(TO, WI, TO, GU, DA, BR))

		


"""
class WTough(object):
	def __init__(self):
		self.model = "Windy Tough"
		self.style = "Road Bike"
		self.weight = 26.00
		self.cost = 700.00
		self.price = (self.cost * markup) + (self.cost)
		self.inv = 15
		
class WHigh(object):
	def __init__(self):
		self.model = "Windy High"
		self.style = "Mountain Bike"
		self.weight = 30
		self.cost = 900.00
		self.price = (self.cost * markup) + (self.cost)
		self.inv = 12
		
class WSleek(object):
	def __init__(self):
		self.model = "Windy Sleek"
		self.style = "City Bike"
		self.weight = 28
		self.cost = 550.00
		self.price = (self.cost * markup) + (self.cost)
		self.inv = 23
		
class WDay(object):
	def __init__(self):
		self.model = "Windy Day"
		self.style = "Country Bike"
		self.weight = 34
		self.cost = 400.00
		self.price = (self.cost * markup) + (self.cost)
		self.inv = 16
		
class WGust(object):
	def __init__(self):
		self.model = "Windy Gust"
		self.style = "Children's Bike"
		self.weight = 24
		self.cost = 150.00
		self.price = (self.cost * markup) + (self.cost)
		self.inv = 5
		
class WBreeze(object):
	def __init__(self):
		self.model = "Windy Breeze"
		self.style = "Fixed Gear Bike"
		self.weight = 22
		self.cost = 600.00
		self.price = (self.cost * markup) + (self.cost)
		self.inv = 3




# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =		SECTION 02
# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =			aliases; 
# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =			list of model names; list of model cost; list of model prices



WTough = WTough()
WHigh = WHigh()
WSleek = WSleek()
WDay = WDay()
WGust = WGust()
WBreeze = WBreeze()

# list of model costs (to produce) and
# list of model prices (including 20% markup)
model_names = [WTough.model, WHigh.model, WSleek.model, WDay.model, WGust.model, WBreeze.model]
model_cost = [WTough.cost, WHigh.cost, WSleek.cost, WDay.cost, WGust.cost, WBreeze.cost]
model_price = [WTough.price, WHigh.price, WSleek.price, WDay.price, WGust.price, WBreeze.price]






# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =		SECTION 03
# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =			the big sort - by price, retain sort, return model names 



# dictionary of name/price to: SORT by price, then return corresponding models


import operator
name_price = {
	WTough.model: WTough.price,
	WHigh.model: WHigh.price,
	WSleek.model: WSleek.price,
	WDay.model: WDay.price,
	WGust.model: WGust.price,
	WBreeze.model: WBreeze.price
}
sorted_name_price = sorted(name_price.items(), key = operator.itemgetter(1))


print "sorted_name_price"
print sorted_name_price
print "print first item in sorted list"
print sorted_name_price


print len(sorted_name_price)

print name_price

for i in name_price(value):
	print i
	
#	for i in range(low_price, hi_price,  -1):
#		print i

"""



print "Hello"



