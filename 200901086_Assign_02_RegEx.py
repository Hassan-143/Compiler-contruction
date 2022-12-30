# Importing the re module for regular expressions.
import re


# Function for Tokenization of the expression.
def tokenize(expression):
    # Building the RegEx pattern.
    pattern = r'\d+|[a-zA-Z]+|\+|\*|\(|\)'
    # OR
    # pattern = r'\d+|\w+|\S'
    tokens = re.findall(pattern, expression)
    return tokens


expression = "3 + (5 * 2)"
tokens = tokenize(expression)
print("\nTokens of the expression are: ", tokens)




