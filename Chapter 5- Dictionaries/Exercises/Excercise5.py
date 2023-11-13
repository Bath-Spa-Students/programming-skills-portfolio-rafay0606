## Excercise 5

# Making dictionaries for each pet & its owner


simba = {
    'animal' : 'Lion',
    'owner' : "Naveed"
}

feathers = {
    'animal' : 'finches',
    'owner' : 'Ahmad'
}

whiskers = {
    'animal' : 'cat',
    'owner' : 'Abubakar'

}

fluffy = {
    'animal' : 'husky dog',
    'owner' : 'Rafay'

}

casy = {
    'animal' : 'Horse',
    'owner' : 'Turab'
}

milo = {
    "animal" : 'Goat',
    'owner' : "Sibtain"
}


# Storing all the above dictionaries in 1 list called pets
pets = [feathers, whiskers, fluffy, casy, milo, simba ]


# Looping the whole list & displaying info about each pet
for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner's Name: {pet['owner']}")
    print("-----------------------")
