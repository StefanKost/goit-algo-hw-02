def check_brackets(expression):
    """
    Checks if the brackets in the expression are balanced.
    Supports: (), [], {}
    """
    stack = []
    # Dictionary of matching pairs
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.append(char)  # push opening bracket to stack
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return "Unbalanced"
            stack.pop()  # correct pair found, remove from stack

    return "Balanced" if not stack else "Unbalanced"


expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }",
    "( 11 )",
    "{ 10 } * ((15)"
]

for expr in expressions:
    result = check_brackets(expr)
    print(f'"{expr}": {result}')
