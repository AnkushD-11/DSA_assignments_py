class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_character(self, char_to_remove):
        # Handle the case where the head node needs to be removed
        while self.head and self.head.data == char_to_remove:
            self.head = self.head.next

        if not self.head:
            return

        current = self.head
        prev = None

        while current:
            if current.data == char_to_remove:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next


# Example usage:
ll = LinkedList()
ll.append('a')
ll.append('b')
ll.append('c')
ll.append('a')
ll.append('d')
ll.append('e')
ll.append('a')

print("Original linked list:")
ll.display()

char_to_remove = 'a'
ll.remove_character(char_to_remove)

print(f"Linked list after removing '{char_to_remove}':")
ll.display()
