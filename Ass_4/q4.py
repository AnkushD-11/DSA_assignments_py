# Write a program to perform insertion and deletion in a given LL

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

    def insert_after(self, prev_data, new_data):
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == prev_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {prev_data} not found.")

    def delete(self, target_data):
        if not self.head:
            print("List is empty.")
            return

        if self.head.data == target_data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == target_data:
                current.next = current.next.next
                return
            current = current.next

        print(f"Node with data {target_data} not found.")

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    print("Original Linked List:")
    linked_list.display()

    linked_list.insert_after(20, 25)
    linked_list.insert_after(10, 15)

    print("Linked List after Insertions:")
    linked_list.display()

    linked_list.delete(20)
    linked_list.delete(15)

    print("Linked List after Deletions:")
    linked_list.display()
