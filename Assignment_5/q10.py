class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoublyLinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

def binary_tree_to_doubly_linked_list(root, doubly_linked_list):
    if root is None:
        return

    binary_tree_to_doubly_linked_list(root.left, doubly_linked_list)

    # Append the current node to the doubly linked list
    doubly_linked_list.append(root.value)

    binary_tree_to_doubly_linked_list(root.right, doubly_linked_list)

# Helper function to display the doubly linked list
def display_doubly_linked_list(dll):
    current = dll.head
    while current:
        print(current.value, end=" <-> ")
        current = current.next
    print("None")

# Create a binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Create an empty doubly linked list
dll = DoublyLinkedList()

# Convert the binary tree to a doubly linked list
binary_tree_to_doubly_linked_list(root, dll)

# Display the doubly linked list
print("Doubly Linked List:")
display_doubly_linked_list(dll)
