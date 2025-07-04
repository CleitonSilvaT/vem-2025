class Solution:
    def isPalindrome(self, head):
        rev = None  
        slow = fast = head  
        while fast and fast.next:
            fast = fast.next.next  
            rev, rev.next, slow = slow, rev, slow.next  
        if fast:
            slow = slow.next  
        while rev and rev.val == slow.val:
            rev = rev.next  
            slow = slow.next  
        return not rev  