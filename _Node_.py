# For this project we will isolate implementation of a recursive algorythm
# The algebraic expression input & output will be as an immutable string
# We want to make the process of evaluation more efficient by using data structures

# No feedback on questions as yet, so we'll proceed without the feedback

class _Node_:
    '''
    This class represents a node in the expression tree.
    '''
    def __init__(self, value):
        '''
        Initializes a new node the given value.

        Argument:
            value: The value of the node, which can be a number (float) or an operator (+, -, *,/).
            '''
        self.value = value
        self.left = None
        self.right = None

def build_tree(expression):
    '''
    Builds an expression tree from a given algebraic expression string.
    Arguments:
         expression: A string representing the algebraic expression (i.e., "2+3*4).

    Returns:
        The root node of the constructed expression tree.

    Raises:
        ValueError: If the expression contains invalid characters.
        '''
    stack = []
    for char in expression:
        if char.isdigit():
            # If the character is a digit, create a node with the numerical value (converted to float).
            stack.append(_Node_(float(char)))
        elif char in "+-*/":
            # If the character is an operator, create a node with the operator symbol.
            node = _Node_(char)
            # Pop the two operands (nodes) from the stack and assign them as left and right children of the operator node.
            node.right = stack.pop()
            node.left = stack.pop()
            # Push the constructed operator node back onto the stack.
            stack.append(node)
        elif char == "(":
            # Left parenthesis is encountered, but we don't need a specific node for it.
            pass
        elif char == ")":
            # Process elements until we encounter the opening parenthesis '('
            while stack[-1].value != "(":
                node = stack.pop()
                top_node = stack.pop()
                top_node.right = node  # The popped node becomes the right child of the top node on the stack.
                stack.append(top_node)
            # Remove the opening parenthesis '(' node from the stack.
            stack.pop()
        else:
            raise ValueError("Invalid character in expression")
            # After processing the entire expression, the root node should be the only element remaining in the stack.
        return stack.pop()

def evaluate(_Node_):
        '''
    Evaluates the expression represented by the given node in the expression tree.

    Arguments:
        _node_: The node of the expression tree to be evaluated.

    Returns:
        The numerical result of evaluating the expression.
    '''
        if isinstance(_Node_.value, float):
            # If the node is a leaf node containing a numerical value, return that valu.
            return _Node_.value
        # Recursively evaluate the left and right subtrees of the current node .

        left = evaluate(_Node_.left)
        right = evaluate(_Node_.right)
        # Perform the operation based on the operator at the current node.
        if _Node_.value == "+":
            return left + right
        elif _Node_.value == "-":
            return left - right
        elif _Node_.value == "*":
            return left * right
        else:
            return left / right


def main():
    """
    Prompts the user for an algebraic expression, builds the expression tree, evaluates it, and prints the result.
    """
    expression = input("Enter an algebraic expression: ")
    try:
        root = build_tree(expression)
        result = evaluate(root)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Invalid expression: {e}")


if __name__ == "__main__":
    main()


