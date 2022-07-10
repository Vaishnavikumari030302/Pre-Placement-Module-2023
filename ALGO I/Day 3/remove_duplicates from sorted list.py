
# Graphically detailed explanation available at https://myleetcodejourney.blogspot.com/2021/01/leet-code-82-remove-duplicates-from.html
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        iterate the linked list using p
            if stack is empty, push p into it
            else check if p.val == stack[-1].val
                if yes, push p into stack
                if not, clear stack if len(stack) > 1 otherwise stack[-1] needs to be added to final result     
        '''
        retHead = ListNode()
        pre = retHead
        p = head
        stack = []
        while(p != None):
            if stack and p.val != stack[-1].val:
                if len(stack) > 1:
                    stack = []
                else:
                    pre.next = stack.pop()
                    pre = pre.next
            stack.append(p)
            p = p.next
        if len(stack) > 1:
            pre.next = None
        if len(stack) == 1:
            pre.next = stack.pop()
        return retHead.next  