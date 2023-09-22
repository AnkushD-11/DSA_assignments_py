# Insertion and Deletion in Doubly LL

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, key, data):
        if not self.head:
            print("Doubly Linked List is empty.")
            return

        new_node = Node(data)
        temp = self.head
        while temp:
            if temp.data == key:
                new_node.prev = temp
                new_node.next = temp.next
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                return
            temp = temp.next

        print("Key not found.")

    def delete(self, key):
        if not self.head:
            print("Doubly Linked List is empty.")
            return

        if self.head.data == key:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

        print("Key not found.")

    def display(self):
        if not self.head:
            print("Doubly Linked List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print()

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(3)
    dll.prepend(0)
    dll.insert_after(1, 2)

    print("Initial Doubly Linked List:")
    dll.display()

    dll.delete(3)
    print("After deleting node with value 3:")
    dll.display()
