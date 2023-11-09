# Medium
# search in rotated sorted array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        # print(start, end, mid)
        if nums[mid] == target:
            return mid

        # в случае когда nums[start:end+1] - повернутый массив
        if nums[end] < nums[start]:

            # если mid попал в левую часть массива (все ее элементы больше правой)
            if nums[mid] > nums[end]:

                # если искомое значение больше конца, значит искомое значение может находиться только в левой части
                if target > nums[end]:
                    if target > nums[mid]:
                        start = mid + 1
                    else:
                        end = mid - 1
                # иначе нужно двигаться к правой части массива
                else:
                    start = mid + 1

            # в слеучае если мы попали в правую часть (все ее части меньше левой)
            elif nums[mid] < nums[start]:
                # если искомое значение больше центра
                if nums[mid] < target:
                    # если значение слева больше искомого значения, то элемент находится в правой части и правее mid
                    if nums[start] > target:
                        start = mid + 1
                    # в ином случае искомое значение в левой части
                    else:
                        end = mid - 1
                # если меньше, то искомое значение находится левее центра, но в правой части массива
                else:
                    end = mid - 1
            else:
                start = mid + 1

        # классический случай
        else:
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

    return -1


def main():
    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 8
    print(search(nums, target))


if __name__ == '__main__':
    main()
