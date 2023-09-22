#Decimal to binary using stack

def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    stack = []

    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.append(str(remainder))
        decimal_num = decimal_num // 2

    binary_result = ""
    while stack:
        binary_result += stack.pop()

    return binary_result

# Example usage:
decimal_number = 15
binary_result = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_result}")
