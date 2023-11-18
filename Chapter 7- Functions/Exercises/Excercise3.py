#Excercise 

def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')


#Calling the function using keyword arguments
make_shirt('large', 'I love Cybersecurity')
make_shirt(message="Keep Grinding!", size='medium')
