"""
I've put each bike model as its own class, with the properties for each bike contained inside that class. 

I then print each model name, which I did manually, although now I think I could've dumped the 
model names into a list and just printed that out.

> > Next, I want to dump the bike types into a dictionary (bike name=key : bike type=value) 
    [name_a:type_a, name_b:type_b, name_c:type_c]

and, using a while statement, ask the customer if s/he is looking for (each) type of bike in the dictionary. 
    answer = "n" or "N"
    while answer is True:
    "Are you looking for [type_a]?"
    "y or n"
    answer = raw_input()
when answer = False, return the key (name_x) to the bike type (type_x) from the dictionary
.
.
.
- From there,  capture all of the customer's information
- Then talk budget, using if statements to get a bike within the customer's budget (comparing budget 
  against bike cost + 20% markup)
- Next, print out the customer's information, type of bike purchased, cost of bike, and how much 
  they saved (money left over from their budget)
- Finally, print out the remaining inventory in the store, including -1 of the model the customer bought

From there, it should be fairly straightforward to grab the classes and throw them into their own file, 
importing that file to start things rolling.

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
- city		  windy-sleek	28 lb	$550		23		?				?
- country	  windy-day		34 lb	$400		16		?				?
- kids'		  windy-gust	24 lb	$150		5		?				?
- fixed gear  windy-breeze	22 lb	$600		3		?				?

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
	print WTough.model + ", the",
	print WHigh.model + ", the",
	print WSleek.model + ", the",
	print WDay.model + ", the",
	print WGust.model + ", and the",
	print WBreeze.model 
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

#  TESTING
# sort prices of bikes in model_pr
print "Sorted order of bike prices (including markup):\n",
price_ascend = sorted(model_price)
print price_ascend

#  TESTING
num_bikes = len(price_ascend)
# length of sorted price list
half_prlist = num_bikes / 2


#  TESTING
# half the length of sorted price list
print "\nHalf_prlist is:"
print half_prlist

#  TESTING
# maximum price in 1st half of sorted price list
median_prlist = max(price_ascend[0:half_prlist])
print "\nMedian price"
print median_prlist


#  TESTING
# price between median price up to not incl max price
print "\nPrices from median up to not incl highest price"
print price_ascend[half_prlist:(num_bikes - 1)]

#  num_bikes = inventory; number_of_bikes is a count var
number_of_bikes = num_bikes


#  TESTING
print "\nAll bike model names sorted by price"
print sorted(model_names)

print "\nBike models except for top-priced model"
print model_names[0:number_of_bikes - 1]



#  INFO
#   FOR INFO ON SORTING LIST OF CLASS OBJECTS:
#  https://www.daniweb.com/software-development/python/code/216631/a-list-of-class-objects-python






cust_budget = raw_input("So, how much did you want to spend?\n")







# if cust_budget is greater than most expensive bike:
def budget_big():
	print cust_budget
	if int(cust_budget) >= int(max(price_ascend)):
		print "Well, we have every style to fit your budget!"
		print "\n your budget is %s" % cust_budget
		print "\n our top-priced bike is %s" % max(price_ascend)
#		wants()
	else:
		budget_queries()
		
		
# if cust_budget is between cost of top bike and next lower-priced bike:
#     --->  change to last-called bike price
def budget_queries():
	x = 1
	number_of_bikes = num_bikes
	print number_of_bikes
	print price_ascend
	print price_ascend[int(number_of_bikes)]
	
	"""
	while x <= number_of_bikes:
		if cust_budget >= price_ascend[(number_of_bikes - x)] and cust_budget < price_ascend[number_of_bikes]:
			print "Yes, we have several models you can check out!"
			x += 1
		else:
			print "We have a top-notch children's model"
 
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
budget_big()




