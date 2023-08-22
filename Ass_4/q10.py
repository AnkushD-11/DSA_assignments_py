#Add two polynomials using linked lists

class Node:
    def __init__(self, coeff=0, exp=0):
        self.coeff = coeff
        self.exp = exp
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coeff, exp):
        new_term = Node(coeff, exp)
        if not self.head:
            self.head = new_term
        else:
            current = self.head
            prev = None
            while current and current.exp > exp:
                prev = current
                current = current.next
            if current and current.exp == exp:
                current.coeff += coeff  # Combine like terms
            else:
                new_term.next = current
                if prev:
                    prev.next = new_term
                else:
                    self.head = new_term

    def add(self, other):
        result = Polynomial()
        current_self = self.head
        current_other = other.head

        while current_self or current_other:
            if current_self and (not current_other or current_self.exp > current_other.exp):
                result.insert_term(current_self.coeff, current_self.exp)
                current_self = current_self.next
            elif current_other and (not current_self or current_self.exp < current_other.exp):
                result.insert_term(current_other.coeff, current_other.exp)
                current_other = current_other.next
            else:
                # coeffs have the same exp, so add them
                result.insert_term(current_self.coeff + current_other.coeff, current_self.exp)
                current_self = current_self.next
                current_other = current_other.next

        return result

    def display(self):
        current = self.head
        while current:
            print(f"{current.coeff}x^{current.exp}", end=" ")
            current = current.next
            if current:
                print("+", end=" ")
        print()

# Example usage:

# Create two polynomials: 2x^3 + 3x^2 + 4x + 1 and 3x^2 + 5x + 2
poly1 = Polynomial()
poly1.insert_term(2, 3)
poly1.insert_term(3, 2)
poly1.insert_term(4, 1)
poly1.insert_term(1, 0)

poly2 = Polynomial()
poly2.insert_term(3, 2)
poly2.insert_term(5, 1)
poly2.insert_term(2, 0)

# Add the two polynomials
result = poly1.add(poly2)

# Display the result: 2x^3 + 6x^2 + 9x + 3
result.display()
