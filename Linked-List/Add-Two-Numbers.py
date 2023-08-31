# Define a class Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummyHead ListNode with value 0 to serve as the starting point of the result linked list
        dummyHead = ListNode(0)
        tail = dummyHead  # Initialize a tail pointer to the dummyHead
        carry = 0  # Initialize the carry to 0 for addition

        # Iterate while there are still digits in l1 or l2 or there's a carry left
        while l1 is not None or l2 is not None or carry != 0:
            # Get the digits from l1 and l2 if available, otherwise use 0
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            # Calculate the sum of digits and the new carry
            sum = digit1 + digit2 + carry
            digit = sum % 10  # Calculate the new digit for the current position
            carry = sum // 10  # Calculate the new carry for the next position

            # Create a new ListNode with the calculated digit
            newNode = ListNode(digit)
            
            # Link the newNode to the tail of the result linked list
            tail.next = newNode
            
            # Move the tail pointer to the newly added node
            tail = tail.next

            # Move to the next nodes in l1 and l2 if available
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # The result linked list starts from the node after dummyHead
        result = dummyHead.next
        dummyHead = None  # Set dummyHead to None to remove its reference

        # Return the result linked list
        return result
