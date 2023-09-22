class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def reverse(self):
        current = self.head
        prev_node = None

        while current:
            # Swap next and prev pointers of the current node
            next_node = current.next
            current.next = prev_node
            current.prev = next_node

            # Move to the next node
            prev_node = current
            current = next_node

        # Update the head to the last node (prev_node)
        self.head = prev_node


# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Original Doubly Linked List:")
dll.display()

dll.reverse()

print("\nReversed Doubly Linked List:")
dll.display()
