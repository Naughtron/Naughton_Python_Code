# Exercise 39: Dictionaries, Oh Lovely Dictionaries
 
# create a dict that has a state and abrevation mapping
states = {'Oregon': 'OR', 'Florida' : 'FL', 'California':'CA', 'New york':'NY', 'Michigan':'MI'}
 
# create a dict with a list of cities within states
cities = {'CA':'San Fran', 'MI':'Detroit', 'FL':'Jacksonville'}
 
# add cities to the dict you just created
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
 
# print out some of the cities by finding them by association
print "-" * 10
print "Ny State has: ", cities['NY'] # prints everything associated with the NY key
print "OR State has: ", cities['OR'] # prints everything associated with the OR key
 
# print out some states
print "-" * 10
print "Michigan has: ", cities[states['Michigan']] # finds the states association "MI" associates it with cities "MI" to find detroit
print "Florida has: ", cities[states['Florida']] # finds the states association "FL" associates it with cities "FL" to find jacksonville
 
# print all the state abbreviations
print "-" * 10
for state, addrev in states.items(): # it so first value in the pair is known as state and second value in the pair is known as abbrev
        print "%s is abbreviated %s" % (state, addrev)
       
# print all the cities in the states dict
print "-" * 10
for abbrev, city in cities.items():
        print "%s has the city %s" % (abbrev, city) # on the fly associate abbrev with the first value in a pair and city with the other
 
# now print out everything at the same time
print "-" * 10
for state, abbrev in states.items():
        print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
 
# how to deal with a state that is not there
print "-" * 10
state = states.get('Texas', None)
if not state: # if the state does not have a matched pair
        print "Sorry, no planet of Texas"
       
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city