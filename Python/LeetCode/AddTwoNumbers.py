# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


# ---------------------------
# Helper functions
# ---------------------------

# Convert Python list → Linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Convert Linked list → Python list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ---------------------------
# Test the solution
# ---------------------------
s = Solution()

# Example 1
l1 = list_to_linkedlist([2,4,3])
l2 = list_to_linkedlist([5,6,4])
res = s.addTwoNumbers(l1, l2)
print("Example 1 Output:", linkedlist_to_list(res))  # [7,0,8]

# Example 2
l1 = list_to_linkedlist([0])
l2 = list_to_linkedlist([0])
res = s.addTwoNumbers(l1, l2)
print("Example 2 Output:", linkedlist_to_list(res))  # [0]

# Example 3
l1 = list_to_linkedlist([9,9,9,9,9,9,9])
l2 = list_to_linkedlist([9,9,9,9])
res = s.addTwoNumbers(l1, l2)
print("Example 3 Output:", linkedlist_to_list(res))  # [8,9,9,9,0,0,0,1]
