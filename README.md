# Compiler Contruction

## Implementation of RegEx
•	Step 1: Tokenization of Expression

The first step in implementing a lexical analyzer is to tokenize the expression. This involves breaking down the string into individual elements such as numbers, symbols, and words. 
For example, the expression “ 3 + (5 * 2) ” can be broken down into the following tokens:
[ '3', '+', '(', '5', '*', '2', ')' ]

•	Step 2: Building Regex for the Expression

The next step is to build a regular expression (regex) for the expression. This allows the lexer to identify and match patterns within the string. 
For example, the regex for the expression “ 3 + (5 * 2) ” might look like this:
r ' \ d+ | [ a-z A-Z ] + | \+ | \* | \ (| \) '
       or
    r  ' \d + | \w + |\S '
This regex will match any alphabetic character (a-z or A-Z) or any special character ( + ,  - ,  * ,  / ,  (  or ) ).

•	Step 3: Tokens of the Expression

The final step is to display the output for tokens of the expression. This is done by looping through the expression and matching each element against the regex. If a match is found, the corresponding tag is displayed. 
For example, in the expression “3 + (5 * 2)”  the following tags would be displayed:
['NUMBER', 'OPERATOR', 'PAREN_OPEN', 'NUMBER', 'OPERATOR', 'NUMBER', 'PAREN_CLOSE']

![image](https://user-images.githubusercontent.com/74555200/210099625-18b1a286-50ea-42dd-8fa0-22880858f0d5.png)


## Implementation of AST 

The AST library of python provides the means to construct an abstract syntax tree of a Python code. This is a useful tool for analyzing, understanding and representing the structure of the code.

An AST is a tree structure that represents the syntactic structure of a program. It consists of nodes, which can be either terminals or non-terminals. Terminals are symbols that cannot be further expanded, such as identifiers, literals, operators, and keywords. Whereas non-terminals are symbols that can be further expanded, such as functions, classes, and variables. Moreover, it provides a set of APIs to construct an abstract syntax tree. The APIs can be used to construct a node and then connect it to other nodes in the tree by also providing methods to traverse the tree and perform various operations on it.

The AST library of python is used in many applications such as code analysis, code refactoring, code generation, and static analysis. It is also used to generate code from a given AST.

![image](https://user-images.githubusercontent.com/74555200/210099728-63747a8b-530b-4657-ba92-8c7a9d2c7e6e.png)

 

