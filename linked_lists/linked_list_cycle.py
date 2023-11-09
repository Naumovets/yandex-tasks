# Easy
# linked list cycle
# https://leetcode.com/problems/linked-list-cycle/

def has_cycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    test_list = []
    while head:
        test_list.append(head)
        head = head.next
        if head in test_list:
            return True
    return False


def main():
    ...


if __name__ == '__main__':
    main()