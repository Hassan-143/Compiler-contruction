# Importing the AST library for syntax tree.
import ast

# Creating a syntax tree.
syntax_tree = ast.parse("print('AST created!')")
print(syntax_tree)

print("The syntax tree is: ")
print(ast.dump(syntax_tree))

# Executing the abstract syntax tree.
exec(compile(syntax_tree, filename="", mode="exec"))

