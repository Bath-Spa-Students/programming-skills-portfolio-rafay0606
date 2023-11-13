## Exercise 2

#Creating a Dictionary/Glossary with the programming words along with their meaning

glossary = {
     'debugging' : 'the process of detecting and removing of existing and potential errors in a software code that can cause it to behave unexpectedly or crash.',
     'string' : 'It is a collection of alphabets, words or other characters. ',
     'algorithm' : 'they are a set of instructions that are executed to get the solution to a given problem ',
     'loop' : 'It means repeating something over and over until a particular condition is satisfied.',
     'list' : 'It is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.'
}

#Printing the words & their meanings from the dictionary/glossary above
for word, meaning in glossary.items():
    print(word + ':')
    print(meaning +  '\n')
