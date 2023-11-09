# Easy
# reverse linked list
# https://leetcode.com/problems/reverse-linked-list/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    result = None
    while head:
        result = ListNode(head.val, result)
        head = head.next
    return result


def main():
    ...


if __name__ == '__main__':
    main()
