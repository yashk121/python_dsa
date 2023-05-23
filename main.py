# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    prev, curr, head = None, None, None
    while (l1 != None and l2 != None):
        sum = l1.val + l2.val
        sum = sum + carry
        carry = int(sum / 10)
        unit = sum % 10
        prev = curr

        curr = ListNode(unit)
        if (prev == None):
            head = curr
            prev = curr
        else:
            prev.next = curr
        l1 = l1.next
        l2 = l2.next
    while (l2 != None):
        sum = l2.val + carry
        carry = int(sum / 10)
        unit = sum % 10
        prev = curr
        curr = ListNode(unit)
        prev.next = curr
    while (l1 != None):
        sum = l1.val + carry
        carry = int(sum / 10)
        unit = sum % 10
        prev = curr
        curr = ListNode(unit)
        prev.next = curr
    if (carry != 0):
        curr.next = ListNode(carry)
    return head


def binarysearch(list, target):
    l = 0
    r = len(list)

    while l <= r:
        m = int((l + r) / 2)
        if list[m] == target:
            return "found"
        elif list[m] < target:
            l = m + 1
        else:
            r = m - 1
    return "Not found"


if __name__ == '__main__':
    l = [3, 5, 8, 9, 23, 36, 67]
    print(binarysearch(l, 3))
