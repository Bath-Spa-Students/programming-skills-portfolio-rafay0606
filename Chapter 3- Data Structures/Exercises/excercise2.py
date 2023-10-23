## Exercise 2: Greetings :ballot_box_with_check:

# list of friends names
names = ["Rafay", "Ahmad", "James", "Sultan", "Khadijah", "Mariez", "Rehman", "Rafay"]

# Personalized Message
message_template = "Hello, {}! Have a great day!"

# Print personalized messages to each person
for name in names:
    personalized_message = message_template.format(name)
    print(personalized_message)
