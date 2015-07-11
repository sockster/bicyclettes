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
- mountain    windy-high	30 lb	$900		12		?				?
- road		  windy-tough	26 lb	$700		15		? (raw_input)	? (raw_input)
- fixed gear  windy-breeze	22 lb	$600		3		?				?
- city		  windy-sleek	28 lb	$550		23		?				?
- country	  windy-day		34 lb	$400		16		?				?
- kids'		  windy-gust	24 lb	$150		5		?				?

"""

# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =		SECTION 01
# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =			setting classes; storing price markup 

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
# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =			welcome message; 



#     WELCOME MESSAGE
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









# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =		SECTION 03
# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =			the big sort - by price, retain sort, return model names 



# dictionary of name/price to: SORT by price, then return corresponding model names


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
# 	bikes_ascend = list of (name, price)
bikes_ascend = sorted_name_price





# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =		SECTION 04
# 		= = = = = = = = = = = = = = = = = = = = = = = = = = =			comparing customer's budget with bike prices 



# currently returning all models for # models available
#	WANT: return only models < cust_budget

out = []
for cust_price in bikes_ascend:
	if cust_price > bikes_ascend:
		out.append(bikes_ascend)
		

cust_budget = raw_input("So, how much did you want to spend?\n")
cust_budget = float(cust_budget)
print "Print out (list)"
print out












"""
#	lo-tech:
# 	if cust_budget is > than max; or < min; else, start price_queries() to determine what is in cust's price range


#cust_budget = raw_input("So, how much did you want to spend?\n")
#cust_budget = float(cust_budget)

def dialog_1():
	print "Well, we have every style to fit your budget!"
	print "\n your budget is %s" % cust_budget
	print "\n our top-priced bike is %s" % max(model_price)

def dialog_2():
	print "Ok, we have several styles to fit your budget."
	print "\nYour budget is %s" % cust_budget

def dialog_3():
	print "We have some really nice kids' bikes over here."
	print "\nYour budget is %s" % cust_budget


def dialog_4():
	print "I'm sorry, we don't have any bike models in your price range,",
	print " but we have plenty of accessories you might be interested in."





cust_budget = raw_input("Your budget here\n")
cust_budget = float(cust_budget)
# price_ascend = prices only
price_ascend = model_price




bike_prices = range(int(min(price_ascend)), int(max(price_ascend)))









def budget():
	x = (len(bikes_ascend) - 1)

# make FOR statement so that FOR each price, compare cust_budget, IF >=, then DIALOG_2(), ELSE, DIALOG_4()
#		for cust_budget in prices_ascend:
	
	if cust_budget >= bike_prices:
		dialog_1()
		
	elif cust_budget <= bike_prices:
		dialog_4()

	else:
#	 cust_budget will be within bike price range:
		price_queries()





def price_queries():
	print "Hello Bike World"

#  here is where the welcome() will be called when other sections are ready
budget()











#   ORIGINAL IF statement for cust_budget > max bike price:
			if cust_budget > max(prices_ascend):
				dialog_1()
				x += 1
				



				
#   TESTING
#		testing x

x = (len(bikes_ascend) - 2)
print x
print prices_ascend[x]




#   TESTING
#		testing the sorted_name_price list

print "sorted_name_price"
print sorted_name_price
print "\nprint first item in sorted list"
print sorted_name_price


print "\nprint length of sorted_name_price list"
print len(sorted_name_price)

v = 20
print "\nIs v (20) > Windy Gust (the lowest price bike)?"
print v > sorted_name_price[0]
print v < sorted_name_price[3]
print sorted_name_price[3]









for i in name_price(value):
	print i
	
#	for i in range(low_price, hi_price,  -1):
#		print i





#  calls 1st budget query (>= top price or < min)

# if cust_budget is >= most expensive bike...	 if not, call 2nd budget query
def budget_big():
	if cust_budget >= max(model_price):
		print "Well, we have every style to fit your budget!"
		print "\n your budget is %s" % cust_budget
		print "\n our top-priced bike is %s" % max(model_price)
#		wants()

# 2nd budget query: if cust_budget < lowest price
	elif cust_budget < min(model_price):
		print "I'm sorry, we don't have any bike models in your price range,",
		print " but we have plenty of accessories you might be interested in."
		
	else:
		budget_mid()
		print "> > To mid-level priced bikes"
		
def budget_mid():
	x = len(sModelprice)

	while cust_budget > sModelprice[x]:
		if cust_budget >= sModelprice[x]:
			budget_found()
		
		else:
			print "Well, we have others"
		x -= 1
			




def spend_budget():
	budget_big()





#   TESTING
#	Trying to call each specific element in sModelprice list to compare to cust_budget
#   Below would use var from len of sModelprice to call specific element in list
print "TESTING"
print "sModelprice[0] :"
print sModelprice[0]
print "len(sModelprice) :"
print len(sModelprice)

x = len(sModelprice)
print "print x (s/b same as above):"
print x
print "print x = x - 2"
x = x - 2
print x
print "print sModelprice[x]:"
print sModelprice[x]
print ""
print ""
print "END OF TESTING"

#	END TESTING



def budget_found():
	print "Ok - we have several styles to fit your budget."
#	print "\n your budget is %s" % cust_budget
#	print "\n our top-priced bike you is %s" % sModelprice[x]






																	error returned is:

sModelprice[x]
Traceback (most recent call last):
  File "bike_sales_3.py", line 253, in <module>
    print sModelprice[x]
IndexError: list index out of range

																		WHY?
																		if sModelprice[0] returns 1st element in sModelprice,
																			and x = len(sModelprice),
																			returning 6,
																			why doesn't sModelprice[x] work?
																			TRIED: x = int(x), but returned same error
print "LOOK HERE"
print sModelprice[5]

#  budget_big()















		> > >			Below are previous attempts at sorting price, retaining the sort, then returning bike names


# THE PLAN - 07.03:
#	sort by price; leave names for now




#  TESTING
# number of bike models
num_bikes = len(model_price)
bikes_budget = num_bikes
# length of price list
print "\nNumber of bike models:"
print num_bikes

# sorted list of bike prices
sModelprice = sorted(model_price)
print "Sorted Model Prices"
print sModelprice







# IMMEDIATELY BELOW: trying to look at each highest price and compare to cust_budget by calling 1 less than len of prices
#		each "round"

# Count in sModelprice
x = (len(sModelprice) - 1)
def budget_mid():
	print sModelprice
	print ""
#	x = 6
	y = (sModelprice[x])
	print "X:",
	print x
	print "Y:",
	print y
	
	hi_price = x - 1
	low_price = x
#	for (sModelprice):
	low_price = int(min(sModelprice))
#	for i in range(low_price, hi_price,  -1):
#		print i





# this print entire range ... could use as "if w/in range..."
# mid-range price queries, w/ "x" = negative count
def budget_mid():
	x = 1
#	while cust_budget <= sModelprice[:: -x]:
#			if cust_budget is less than top price and greater than next highest price
	Int_sModelprice_min = int(min(sModelprice))
	Int_sModelprice_max = int(max(sModelprice))
	print Int_sModelprice_min
	print Int_sModelprice_max
	for budget_guess in range(Int_sModelprice_min, Int_sModelprice_max):
		print range(budget_guess)







#   @@@@@@@@


# spend_budget()
budget_mid()






# THE PLAN - 07.02:
#	sort class following: http://www.programmingforums.org/thread26556.html
# FAIL.    ...AGAIN

model_price_COPY = model_price

# dictionary of model-to-price
model_nPrice = {
	WTough.model: WTough.price,
	WHigh.model: WHigh.price,
	WSleek.model: WSleek.price,
	WDay.model: WDay.price,
	WGust.model: WGust.price,
	WBreeze.model: WBreeze.price
}


modelPrice = list()
modelPrice.append(model_nPrice("WTough", "700.00"))
modelPrice.append(model_nPrice("WHigh", "900.00"))
modelPrice.append(model_nPrice("WSleek", "550.00"))
modelPrice.append(model_nPrice("WDay", "400.00"))
modelPrice.append(model_nPrice("WGust", "150.00"))
modelPrice.append(model_nPrice("WBreeze", "600.00"))







sort_list = []
for class_object in modelPrice:
	print class_object.model + ": $" + class_object.price
	sort_list.append( [class_object.price, class_object.model, class_object])
	
sort_list.sort()
print "\nAfter sort: \n"
for rec in sort_list:
	class_object = rec[2]
	print class_object.model + ": $" + class_object.price
	

#	Attempts at sorting dictionaries - FAIL
testing = {
	"one": "one-1",
	"four": "four-4",
	"three": "three-3",
	"two": "two-2"
}

values = testing.values()
STesting = sorted(values)
keys = testing.keys()
#  sKeys = keys[STesting]

print "These are the keys to the sorted values:"
# print sKeys




print "This is the dictionary as written:"
print testing
print "\nThis is the dictionary sorted() - which sorts by keys (presum. by default):"
print sorted(testing)
print "\nThis is the dictionary sorted(testing.value):"
print sorted(testing.values())


print "This is model_nPrice mod"
print model_nPrice
print "\nThese are the model_nPrice keys"
print model_nPrice.keys()
print "\nThese are the model_nPrice values"
print model_nPrice.values()

sorted(model_nPrice.values())
print "This is sorted model_nPrice mod"
print model_nPrice


"""






























"""
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





print "Print model_price[3]"
print model_price[3]
models_by_name = sorted(model_price)
print "Print model_price SORTED by price"
print models_by_name
list(models_by_name)
print ""
print ""







#  INFO ON SORTING DICIONARY
#   http://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/


print "list of name_price dictionary:"
print list(name_price)
print ""
print "sorted(name_price) ... defaults to sorting by key: same as sorted(name_price.keys())"
print sorted(name_price)
print ""
print ""
print "sorted(name_price.values())"
print sorted(name_price.values())
print ""
print ""
print "Is the last sort retained? I'll just call name_price"
print name_price
print ""
print ""
print "what happens if I store in a var? will order be stored?!"
SName_price = sorted(name_price.values())
NameList = name_price

NewName = sorted(name_price)
print "NwName"
print NewName



print sorted(SName_price)
print SName_price
print ""
print ""




for value in model_price:
	print "%s.%s" % (model_price)
#  ===== >  how to get class (bike) name from sorted by price list (model_price): DICTIONARY


#   > > > > > > > > > > > > > > > > > > > c/b deleted  (below)


#   NOT RETAINING SORT ORDER
print "sorted by values?  No"
sorted(name_price.values())
print "sorted by names?  No"
print name_price.keys()



#   NOT RETAINING SORT ORDER
#  TESTING: interesting but not working (for another time)
# sort prices of bikes in model_pr
print "Sorted order of bike prices (including markup):\n",
model_price.sort()

#   NOT RETAINING SORT ORDER
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
print ""
print ""

#   > > > > > > > > > > > > > > > > > > > c/b deleted  (above)


	
	
	
	
	
print "Dictionary of models - keys"
print name_price.keys()

print "\nDictionary of prices - values"
print name_price.values()

namePrice = sorted(name_price.values())
namePrice.sort()
for value in namePrice:
	print "%s: %s" % (value, name_price[value])
#	INFO
#  http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/












#  TESTING
# half the length of sorted price list
half_prlist = num_bikes / 2
print "\nHalf_prlist is:"
print half_prlist


#  TESTING
# maximum price in 1st half of sorted price list
median_prlist = max(price_ascend[0:half_prlist])
print "\nMedian price"
print median_prlist


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





		


number_of_bikes = 6
# num_bikes
print number_of_bikes
print price_ascend
print price_ascend[:(number_of_bikes - 1)]
countdown = price_ascend[:(number_of_bikes - 1)]


#  ==== > Right now stuck in endless loop of "else" statement

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
 










#    MODEL BIKE QUERIES (FOR TOP-PRICED BUDGET ONLY)
 ======== >			SAVE for completed price query def
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


print "Hello"
