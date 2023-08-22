#Detect a loop in the linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectLoop(head):
    p = head
    q = head
    
    while q and q.next:
        p = p.next            # Move p pointer by one step
        q = q.next.next       # Move q pointer by two steps
        
        if p == q:
            return True  # Loop detected
        
    return False  # No loop detected

# Create a sample linked list with a loop: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (loop starts here)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next  # Creating a loop

has_loop = detectLoop(head)

if has_loop:
    print("Loop detected in the linked list.")
else:
    print("No loop detected in the linked list.")
