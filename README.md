### Algebraic Expression Tree Calculator
This project implements a calculator that evaluates algebraic expressions using an expression tree data structure. The code is designed for efficiency and clarity.

#### Features:

Supports basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/).
Handles parentheses correctly for proper operator precedence.
Provides clear error handling for invalid expressions.
Requirements:

Python 3.x

#### How to Use:

Clone or download the repository.
Run python main.py from the command line.
Enter an algebraic expression (e.g., "2+(3*4)").
The program will evaluate the expression and print the result.

#### Example:

Enter an algebraic expression: 2+(3*4)
Result: 14

#### Code Structure:

_Node_.py: Defines the _Node_ class representing a node in the expression tree, containing a value (number or operator) and references to left and right child nodes.
build_tree.py: Implements the build_tree function that parses a given algebraic expression string and constructs the corresponding expression tree. It uses a stack to handle operator precedence and parentheses.
evaluate.py: Contains the evaluate function that performs a recursive evaluation of the expression tree. It traverses the tree, evaluating leaf nodes (numbers) and applying operators to child nodes until reaching the root, which holds the final result.
main.py: The main entry point of the program. It prompts the user for an expression, builds the tree, evaluates it, and prints the result. Error handling is included to catch invalid expressions.
