def find_mid(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    end = len(nums) - 1
    start = 0

    while start <= end:
        mid = (start + end) // 2

        if nums[start] <= nums[end]:
            return nums[start]

        if nums[mid] < nums[end]:
            end = mid
        elif nums[mid] > nums[start]:
            start = mid + 1
        else:
            return nums[end]


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(find_mid(nums))


if __name__ == '__main__':
    main()
