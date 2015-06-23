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




store = "Wheely Good"
tax = .20
		
# using Classes by Bike Model:

class WTough(object):
	def __init__(self):
		self.model = "Windy Tough"
		self.style = "Road Bike"
		self.weight = 26.00
		self.cost = 700.00
		self.price = (WTough.cost * tax) + WTough.cost
		self.inv = 15
		
class WHigh(object):
	def __init__(self):
		self.model = "Windy High"
		self.style = "Mountain Bike"
		self.weight = 30
		self.cost = 900.00
		self.price = (WHigh.cost * tax) + WHigh.cost
		self.inv = 12
		
class WSleek(object):
	def __init__(self):
		self.model = "Windy Sleek"
		self.style = "City Bike"
		self.weight = 28
		self.cost = 550.00
		self.price = (WSleek.cost * tax) + WSleek.cost
		self.inv = 23
		
class WDay(object):
	def __init__(self):
		self.model = "Windy Day"
		self.style = "Country Bike"
		self.weight = 34
		self.cost = 400.00
		self.price = (WDay.cost * tax) + WDay.cost
		self.inv = 16
		
class WGust(object):
	def __init__(self):
		self.model = "Windy Gust"
		self.style = "Children's Bike"
		self.weight = 24
		self.cost = 150.00
		self.price = (WGust.cost * tax) + WGust.cost
		self.inv = 5
		
class WBreeze(object):
	def __init__(self):
		self.model = "Windy Breeze"
		self.style = "Fixed Gear Bike"
		self.weight = 22
		self.cost = 600.00
		self.price = (WBreeze.cost * tax) + WBreeze.cost
		self.inv = 3











WTough = WTough()
WHigh = WHigh()
WSleek = WSleek()
WDay = WDay()
WGust = WGust()
WBreeze = WBreeze()
model_names = [WTough.model, WHigh.model, WSleek.model, WDay.model, WGust.model, WBreeze.model]


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


####     START HERE - DUMP INTO LIST (or dict?) SORT BY PRICE, BEGIN MODEL ELIMS BY BUDGET
model_price = {"T": WTough.price, "H": WHigh.price, "S": WSleek.price, "D": WDay.price, "G": WGust.price, "B": WBreeze.price}
model_pr = [WTough.price, WHigh.price, WSleek.price, WDay.price, WGust.price, WBreeze.price]

"""
smallIndex = model_price.values().index(min(a.values()))
smallKey = model_price.keys()[smallIndex]

JUST CHECKING
"""



"""
def budget():

	print ""
	print ""
	print "So, what kind of budget do you have in mind?"
	print ""
	c_budget = raw_input()
		if c_budget >= 900:
			print "Well, we have every style to fit your budget!"
			wants()
		elif c_budget >= 700 and < 900:
			print "


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
	
	

welcome()


wants()

#   OH WAIT! THE ASSIGNMENT IS FOR THE CUST TO SELECT BIKE BASED ON PRICE!!!
# 		NEXT STEP, INSERT IF STMTN, 
# 		IF "WELL, I ONLY CAN AFFORD"
#  ---- WHICH THEN SELECTS THE BIKE MODEL
# ELSE, "MONEY'S NO OBJECT - WHAT TYPES OF BICYCLES DO YOU HAVE?"
#  ---- WHICH THEN GOES INTO THE TYPES OF BICYCLES QUESTIONING"

#


