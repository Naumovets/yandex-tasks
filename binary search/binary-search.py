# Easy
# binary search
# https://leetcode.com/problems/binary-search/

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    end = len(nums) - 1
    start = 0
    while start <= end:
        index = (start + end) // 2
        if nums[index] == target:
            return index
        elif nums[index] < target:
            start = index + 1
        elif nums[index] > target:
            end = index - 1
    return -1


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target))


if __name__ == '__main__':
    main()