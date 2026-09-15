# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = None
        head1= list1
        head2 = list2

        while head1 is not None or head2 is not None:
            if head1 is None and head2 is not None:
                if merged_head is None:
                    merged_head = head2
                    merged = merged_head 
                    return merged_head
                merged.next = head2
                merged = merged.next
                head2 = head2.next   
                continue
                 
            if head2 is None and head1 is not None:
                if merged_head is None:
                    merged_head = head1
                    merged = merged_head 
                    return merged_head
                merged.next = head1
                merged = merged.next
                head1 = head1.next   
                continue

            print(head1.val, head2.val)
            if head1.val <= head2.val:
                if merged_head is None: 
                    merged_head = head1
                    merged = merged_head
                    head1 = head1.next
                    continue
                merged.next = head1
                merged = merged.next
                head1 = head1.next
            else:
                if merged_head is None: 
                    merged_head = head2
                    merged = merged_head
                    head2 = head2.next
                    continue
                merged.next = head2
                merged = merged.next
                head2 = head2.next               
        return merged_head