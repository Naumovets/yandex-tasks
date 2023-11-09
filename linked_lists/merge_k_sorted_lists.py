# Hard
# merge-k-sorted-lists
# https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """

    if lists:
        temp_list = []

        for list_node in lists:
            temp = list_node
            if temp:
                temp_list.append(temp.val)
                while temp.next:
                    temp = temp.next
                    temp_list.append(temp.val)
        if len(temp_list) > 0:
            temp_list = sorted(temp_list)
            result_list_node = ListNode(temp_list[0])
            temp_list_node = result_list_node

            for index in range(len(temp_list) - 1):
                temp_list_node.next = ListNode(temp_list[index + 1])
                temp_list_node = temp_list_node.next

            return result_list_node
    return None


def main():
    ...


if __name__ == '__main__':
    main()
