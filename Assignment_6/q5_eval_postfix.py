def evaluate_postfix(expression):
    stack = []

    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")

            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero is not allowed")
                result = operand1 / operand2

            stack.append(result)
        else:
            raise ValueError("Invalid character in postfix expression")

    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Invalid postfix expression")

# Example usage:
postfix_expression = "23*5+"
result = evaluate_postfix(postfix_expression)
print(f"Result of postfix expression {postfix_expression} is {result}")
