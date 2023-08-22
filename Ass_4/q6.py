'''Given a single linked list of size N. The task is to left-shift the linked list by k nodes, where k is a given positive integer smaller than 
   or equal to length of the linked list.'''
   
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def leftShiftLinkedList(head, k):
    if not head or k == 0:
        return head

    # Step 1: Find the length of the linked list
    length = 1
    current = head
    while current.next:
        length += 1
        current = current.next

    # Step 2: Calculate the effective shift value
    k = k % length

    if k == 0:
        # No need to shift if k is a multiple of the length
        return head

    # Step 3: Traverse to the (N - k)th node
    current = head
    for _ in range(length - k - 1):
        current = current.next

    # Step 4: Update pointers to perform the left shift
    new_head = current.next
    current.next = None
    current = new_head
    while current.next:
        current = current.next
    current.next = head

    return new_head

# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2

new_head = leftShiftLinkedList(head, k)

# The new linked list after left-shifting by 2 nodes: 3 -> 4 -> 5 -> 1 -> 2
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
