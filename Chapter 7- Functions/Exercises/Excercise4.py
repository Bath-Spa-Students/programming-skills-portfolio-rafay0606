#Excercise 4

#Using default size 'Large'
def make_shirt(text_message, size = 'Large'):
    print(" I want a size {0} shirt that says {1}".format(size, text_message))
    
#Specifying the T-shirt size & their text message 
make_shirt("'Keep Grinding'")
make_shirt(size = 'medium', text_message = 'Keep Grinding')
make_shirt(size='small', text_message='Work Smart Not Hard')
