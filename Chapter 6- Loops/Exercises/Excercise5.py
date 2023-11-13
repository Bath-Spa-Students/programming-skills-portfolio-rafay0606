# List of sandwich orders, including 'pastrami'
sandwich_orders = [
    'Pastrami', 'chicken','chicken cheese' 'grilled cheese', 'Pastrami', 'turkey',
      'roast beef', 'Chilli', 'Pastrami']

# List to store finished sandwiches
finished_sandwiches = []

# Informing the customer that pastrami is not available today
print("I'm sorry, we're all out of pastrami today.")

# Removing all occurrences of 'pastrami' from the sandwich_orders list
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Continuing making sandwiches until the sandwich_orders list is not empty
while sandwich_orders:
    # Popping the last sandwich order from the list
    current_sandwich = sandwich_orders.pop()

    print("I'm working on your " + current_sandwich + " sandwich.")

    # Add the finished sandwich to the finished_sandwiches list
    finished_sandwiches.append(current_sandwich)

# Checking through the finished_sandwiches list and print a message for each
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
