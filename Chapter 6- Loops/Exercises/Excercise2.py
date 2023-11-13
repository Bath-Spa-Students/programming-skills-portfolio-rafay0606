#Excercise 2

# Prompting the user for their age
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

# Starting an infinite loop to continuously get user input
while True:
    age = input(prompt)

    # Checking if the user wants to quit
    if age == 'quit':
        break
    age = int(age)

    # Check different age ranges and print messages accordingly
    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
