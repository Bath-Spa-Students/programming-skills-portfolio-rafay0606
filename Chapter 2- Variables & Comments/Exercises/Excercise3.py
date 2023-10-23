## Exercise 3: Stripping Names :ballot_box_with_check:

# Define a person's name with leading and trailing whitespace characters
name_with_whitespace = "\t Syed Abdul Rafay \n"

# Print the name once to display the whitespace around the name
print(name_with_whitespace)

# Use each stripping function to remove the whitespace
name_stripped_left = name_with_whitespace.lstrip()
name_stripped_right = name_with_whitespace.rstrip()
name_stripped_both = name_with_whitespace.strip()

# Print the stripped names
print("Using lstrip():", name_stripped_left)
print("Using rstrip():", name_stripped_right)
print("Using strip():", name_stripped_both)
