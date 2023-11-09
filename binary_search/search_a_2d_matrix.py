# Medium
# search a 2d matrix
# https://leetcode.com/problems/search-a-2d-matrix/

def search_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    # Проходим по каждой из строк матрицы и с помощью
    # классического бинарного поиска ищем в каждой из них элемент
    for i in range(len(matrix)):
        result = search(matrix[i], target)
        if result:
            return True
    return False


# Классический бинарный поиск
def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        if nums[mid] == target:
            return True
    return False


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(search_matrix(matrix, target))


if __name__ == '__main__':
    main()
