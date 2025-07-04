class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = curr = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
      val1 = l1.val if l1 else 0
      val2 = l2.val if l2 else 0
      sum = val1 + val2 + carry
      carry = sum // 10
      curr.next = ListNode(sum % 10)
      curr = curr.next
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
    return dummy.next