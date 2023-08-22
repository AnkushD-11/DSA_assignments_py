# Merge two sorted Linked List

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
        p = self.head
        while p.next:
            p = p.next
        p.next = new_node

    def display(self):
        p = self.head
        while p:
            print(p.data, end=" -> ")
            p = p.next
        print("None")

def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    p1 = list1.head
    p2 = list2.head

    while p1 and p2:
        if p1.data < p2.data:
            merged_list.append(p1.data)
            p1 = p1.next
        else:
            merged_list.append(p2.data)
            p2 = p2.next

    while p1:
        merged_list.append(p1.data)
        p1 = p1.next

    while p2:
        merged_list.append(p2.data)
        p2 = p2.next

    return merged_list

# Example usage
if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(5)
    list1.append(10)
    list1.append(15)

    list2 = LinkedList()
    list2.append(2)
    list2.append(8)
    list2.append(12)

    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()

    merged_list = merge_sorted_lists(list1, list2)
    print("Merged Sorted List:")
    merged_list.display()
