#create a mapping of state to abbreviatiion

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print( '-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Floriad's abbreviation is: ",states['Florida'])

print('-'*50)
for abbrev, city in cities.items():
	print("%s has the city %s" % (abbrev, city))

print('*'*50)
for state, abbrev in states.items():
	print("%s state is abbreviated %s and has city %s" % 
	(state,abbrev, cities[abbrev]))

print('*'*50)
for state, abbrev in states.items():
        print("%s state is abbreviated %s and has city %s" %
        (state,abbrev, cities.get(abbrev)))

#cities.get()==cities[]

