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
- numbr of each model after customer purchase




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
- mountain    windy-high	30 lb	$900		12		?				?
- road		  windy-tough	26 lb	$700		15		? (raw_input)	? (raw_input)
- fixed gear  windy-breeze	22 lb	$600		3		?				?
- city		  windy-sleek	28 lb	$550		23		?				?
- country	  windy-day		34 lb	$400		16		?				?
- kids'		  windy-gust	24 lb	$150		5		?				?

"""



markup = .20


		
# using Classes by Bike Model:

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






WTough = WTough()
WHigh = WHigh()
WSleek = WSleek()
WDay = WDay()
WGust = WGust()
WBreeze = WBreeze()
model_names = [WTough.model, WHigh.model, WSleek.model, WDay.model, WGust.model, WBreeze.model]


store = "Wheely Good"

def welcome():
	print ""
	print ""
	print "Welcome to %s!" % store
	print ""

	print "We have many bicycles - whatever you're looking for"
	print ""
	print "Our models are:"
	print "the",
	print model_names
	print ""
	print ""


# list of model costs (to produce) and
# list of model prices (including 20% markup)
model_cost = [WTough.cost, WHigh.cost, WSleek.cost, WDay.cost, WGust.cost, WBreeze.cost]
model_price = [WTough.price, WHigh.price, WSleek.price, WDay.price, WGust.price, WBreeze.price]

#  TESTING
# print cost to produce each bike
print "Original order of bike costs:\n",
print model_cost
print ""

#  TESTING
# print prices of bikes in original order
print "Original order of bike prices (including markup: cost + 20%):\n",
print model_price
print ""




#  ===== >  how to get class (bike) name from sorted by price list (model_price): DICTIONARY

#  TESTING: interesting but not working (for another time)
# sort prices of bikes in model_pr
print "Sorted order of bike prices (including markup):\n",
model_price.sort()
import itertools
name_ascend = model_price.__class__.__name__
print name_ascend
print ""
print ""
price_ascend = model_price
print ""
print ""
print ""

#   NOT RETAINING SORT ORDER
print "\nprice_ascend names - s/b sorted by price, not name"
print price_ascend








name_price = {
	WTough.model: WTough.price,
	WHigh.model: WHigh.price,
	WSleek.model: WSleek.price,
	WDay.model: WDay.price,
	WGust.model: WGust.price,
	WBreeze.model: WBreeze.price
}

print "Dictionary of models"
print name_price.keys()

print "\nDictionary of prices"
print name_price.values()

namePrice = name_price.values()
namePrice.sort()
for value in namePrice:
	print "%s: %s" % (value, name_price[value])
#	INFO
#  http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/














#  TESTING
num_bikes = len(model_price)
# length of price list
print "\nNumber of bike models:"
print num_bikes


#  TESTING
# half the length of sorted price list
half_prlist = num_bikes / 2
print "\nHalf_prlist is:"
print half_prlist

"""
#  TESTING
# maximum price in 1st half of sorted price list
median_prlist = max(price_ascend[0:half_prlist])
print "\nMedian price"
print median_prlist
"""


#  TESTING
#  num_bikes = inventory; number_of_bikes is a count var
number_of_bikes = num_bikes

#  TESTING
# price between median price up to not incl max price
print "\nPrices from median up to not incl highest price"
print price_ascend[half_prlist:(num_bikes - 1)]

#  TESTING
print "\nAll bike model names sorted by price"
print sorted(model_names)

print "\nBike models except for top-priced model"
print model_names[0:number_of_bikes - 1]



#  INFO
#   FOR INFO ON SORTING LIST OF CLASS OBJECTS:
#  https://www.daniweb.com/software-development/python/code/216631/a-list-of-class-objects-python
#	CLEAR EXAMPLE ON ENUM TYPES:
#  http://www.saltycrane.com/blog/2012/10/python-enum-types/





cust_budget = raw_input("So, how much did you want to spend?\n")







# if cust_budget is greater than most expensive bike:
def budget_big():
	print cust_budget
	if cust_budget >= max(price_ascend):
		print "Well, we have every style to fit your budget!"
		print "\n your budget is %s" % cust_budget
		print "\n our top-priced bike is %s" % max(price_ascend)
#		wants()
	else:
#		budget_queries()
		print "Not big budget"
	
		


number_of_bikes = 6
# num_bikes
print number_of_bikes
print price_ascend
print price_ascend[:(number_of_bikes - 1)]
countdown = price_ascend[:(number_of_bikes - 1)]

"""
==== > Right now stuck in endless loop of "else" statement

# if cust_budget is between cost of top bike and next lower-priced bike:
#     --->  change to last-called bike price
def budget_queries():
	number_of_bikes = 6
	while number_of_bikes > 0:
		high_cost = max(price_ascend[:number_of_bikes])
		low_cost = max(price_ascend[:(number_of_bikes - 1)])
	
	
		if cust_budget >= low_cost and cust_budget < high_cost:
			print "Yes, we have several models you can check out!"
			number_of_bikes -= number_of_bikes
		else:
			print "We have a top-notch children's model"
 
"""

"""
#		Ask what type of bike - to figure out model

def wants():
	model_styles = [WTough.style, WHigh.style, WSleek.style, WDay.style, WGust.style, WBreeze.style]
	mod_num = int(0)

	print "Do you know what type you're looking for?"
	ques = raw_input("Please type Y or N:\n")

#  CALLS each model style by number in list, using var mod_num as (number in list)		
	while mod_num <= 6:
		print "Do you want a",
		print model_styles[(mod_num)],
		print "?"
		answ = raw_input("Y or N?\n")

#  IF YES, calls final model name by final number in list, using var mod_num as (number in list)
#	then cancels mod_num count loop by setting mod_num > 6		
		if answ == "y":
			print "Ok, that would be our " + model_names[(mod_num)],
			print "model"
			mod_num = 7

#  IF NO, adds 1 to mod_num to continue loop to ask about next model
		else:
			print "Oh. Well you probably want something else."
			mod_num += 1
	





	

#    Commenting out for testing
welcome()
# budget_big()




budget_queries()
"""
