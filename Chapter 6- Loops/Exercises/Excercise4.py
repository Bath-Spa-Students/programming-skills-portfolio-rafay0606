#Excercise 4 

# List of sandwich orders
sandwich_orders = ['chicken','chicken cheese' 'grilled cheese', 'turkey', 'roast beef', 'Chilli']

# List to store finished sandwiches
finished_sandwiches = []

# Continue making sandwiches until the sandwich_orders list is not empty
while sandwich_orders:
    # Popping the last sandwich order from the list
    current_sandwich = sandwich_orders.pop()

    # Displaying a message indicating that the current sandwich is being worked on
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

# Iterate through the finished_sandwiches list and print a message for each
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
