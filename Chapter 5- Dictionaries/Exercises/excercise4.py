# Making a dictionary containing there country & its names
rivers = {
    'Nile' : 'Egypt',
    'Mississippi' : 'United States',
    'Yangtze' : 'China'
}

# Using loop to display sentence of each river
for river, country in rivers.items():
    print(f'the {river} is running through {country}.  ') 


# Using loop to display river name in the glossary
print("\nRivers:")
for river in rivers.keys():
    print(river)

# Using loop to display name of country in the glossary
print("\nCountries:")
for country in rivers.values():
    print(country)



