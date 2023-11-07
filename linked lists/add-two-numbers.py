# Medium
# add two numbers
# https://leetcode.com/problems/add-two-numbers/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    s = 0
    k = 0
    while l1 is not None or l2 is not None:
        if l1 is not None:
            s += l1.val * 10 ** k
            l1 = l1.next
        if l2 is not None:
            s += l2.val * 10 ** k
            l2 = l2.next
        k += 1
    result = ListNode()
    head = result
    result.val = s % 10
    s /= 10
    while s > 0:
        result.next = ListNode()
        result = result.next
        result.val = s % 10
        s /= 10
    return head


def main():
    ...


if __name__ == '__main__':
    main()