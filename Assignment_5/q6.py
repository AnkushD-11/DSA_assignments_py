class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def display(self):
        if self.is_empty():
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            return

        if position == 0:
            last_node = self.head.prev
            new_node.next = self.head
            new_node.prev = last_node
            self.head.prev = new_node
            last_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            count = 0
            while count < position - 1 and current.next != self.head:
                current = current.next
                count += 1

            if count < position - 1:
                print("Invalid position")
                return

            next_node = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = next_node
            next_node.prev = new_node

    def delete_at_position(self, position):
        if self.is_empty():
            print("List is empty")
            return

        if position == 0:
            last_node = self.head.prev
            if self.head.next == self.head:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = last_node
                last_node.next = self.head
        else:
            current = self.head
            count = 0
            while count < position and current.next != self.head:
                current = current.next
                count += 1

            if count < position:
                print("Invalid position")
                return

            prev_node = current.prev
            next_node = current.next
            prev_node.next = next_node
            next_node.prev = prev_node


# Example usage
dll = DoublyCircularLinkedList()
dll.insert_at_position(10, 0)
dll.insert_at_position(20, 1)
dll.insert_at_position(30, 1)
dll.display()  # Output: 10 30 20

dll.delete_at_position(1)
dll.display()  # Output: 10 20
