def is_balanced(expression):
    stack = []

    for char in expression:
        if char in "(":
            stack.append(char)
        elif char in ")":
            # Check if the stack is empty or if the top of the stack does not match the closing bracket
            if not stack or not is_matching(stack.pop(), char):
                return False

    # After processing all characters, the stack should be empty if the expression is balanced
    return len(stack) == 0

def is_matching(opening, closing):
    # Helper function to check if the opening and closing brackets match
    return (opening == '(' and closing == ')')

# Example usage:
expression1 = "(())"
expression2 = "(()"

print("Expression 1 is balanced:", is_balanced(expression1))
print("Expression 2 is balanced:", is_balanced(expression2))
