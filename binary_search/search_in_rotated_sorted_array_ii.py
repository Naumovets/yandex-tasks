def search(nums: list, target: int) -> bool:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return True

        # Классический бинарный поиск
        if nums[start] < nums[end]:
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        # В случае перевернутого списка
        else:
            if nums[start] == nums[mid] == nums[end]:
                start += 1
                end -= 1
            # Если попадаем в левую часть списка
            elif nums[mid] > nums[end]:
                # Искомое значение между start и mid
                if nums[mid] > target > nums[end]:
                    end = mid - 1
                # Искомое значение правее mid
                else:
                    start = mid + 1

            # Если попадаем в правую часть списка
            else:
                # Может быть 2 случая, когда target больше nums[mid], потому что target правее nums[mid],
                # либо target больше nums[mid] потому что он находится в левой части списка

                # target правее nums[mid]
                if nums[end] >= target > nums[mid]:
                    start = mid + 1
                # target левее nums[mid]
                else:
                    end = mid - 1
    return False


def main():
    # Алгоритм не работает на входных данных [1,0,1,1,1] и [4,0,1,1,1], т.е там где большое количество повторений
    # и не понятно в какую сторону двигаться, видимо необходимо разделить код пополам
    nums = [0,4]
    print(search(nums, 4))


if __name__ == '__main__':
    main()
