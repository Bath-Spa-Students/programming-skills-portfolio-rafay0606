#Excercise 5

#Assigning country as default value
def describe_city(city, country='Pakistan'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Karachi')
describe_city('Rafay', 'Lahore')
describe_city('Sialkot')
