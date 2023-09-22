# Insertion and Deletion in single LL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def insert_after(self, key, data):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        new_node = Node(data)
        temp = self.head
        while True:
            if temp.data == key:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                print("Key not found.")
                return

    def delete(self, key):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            return

        temp = self.head
        while True:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next
            if temp == self.head:
                print("Key not found.")
                return

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)

    print("Initial Circular Linked List:")
    cll.display()

    cll.insert_after(2, 4)
    print("After inserting 4 after 2:")
    cll.display()

    cll.delete(1)
    print("After deleting node with value 1:")
    cll.display()
