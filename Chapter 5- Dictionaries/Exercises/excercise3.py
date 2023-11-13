## Exercise 3

# Glossary dictionary with programming words and their meanings

glossary = {
     'debugging' : 'the process of detecting and removing of existing and potential errors in a software code that can cause it to behave unexpectedly or crash.',
     'string' : 'It is a collection of alphabets, words or other characters. ',
     'algorithm' : 'they are a set of instructions that are executed to get the solution to a given problem ',
     'loop' : 'It means repeating something over and over until a particular condition is satisfied.',
     'list' : 'It is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.',
     'syntax': 'The set of rules that defines the combinations of symbols that are considered to be correctly structured programs in a specific programming language.',
     'dictionary': 'A collection which is unordered, changeable, and indexed. No duplicate members.',
     'API': 'Application Programming Interface; a set of rules and protocols for building and interacting with software applications.',
     'variable': 'A container for storing data values.',
     'tuple' : 'An immutable, ordered collection of elements, usually of different data types, enclosed within parentheses.'
     
}

# Printing each word and its meaning using a loop
for word, meaning in glossary.items():
    print(word + ': ' + meaning + '\n')