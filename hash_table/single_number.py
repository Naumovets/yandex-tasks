# Easy
# single number
# https://leetcode.com/problems/single-number/

def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    xor = 0
    for num in nums:
        xor ^= num
    return xor


def main():
    nums = [2, 2, 1]
    print(single_number(nums))
    nums = [4, 1, 2, 1, 2]
    print(single_number(nums))
    nums = [1]
    print(single_number(nums))


if __name__ == '__main__':
    main()
