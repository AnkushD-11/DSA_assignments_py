# Tower of Hanoi using stack in python

def tower_of_hanoi(n, source, auxiliary, target):
    stack = []  
    stack.append((n, source, auxiliary, target))

    while stack:
        n, source, auxiliary, target = stack.pop()

        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
        else:
            stack.append((n - 1, auxiliary, source, target))
            stack.append((1, source, auxiliary, target))
            stack.append((n - 1, source, target, auxiliary))

# Example usage:
tower_of_hanoi(3, 'A', 'B', 'C')
