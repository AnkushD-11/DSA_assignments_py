def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char in "+-*/^":  # Operator
            while (stack and stack[-1] in "+-*/^" and
                   precedence[char] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(char)
        elif char == '(':  # Left parenthesis
            stack.append(char)
        elif char == ')':  # Right parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()

    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Example usage:
infix_expression = "a + b * (c - d) / e ^ f"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix expression:", infix_expression)
print("Postfix expression:", postfix_expression)
