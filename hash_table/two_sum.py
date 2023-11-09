# Квадратичная сложность
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]


# Сложность линейная
def two_sum_hash(nums, target):
    hash = {num: (0, []) for num in nums}
    for i in range(len(nums)):
        hash[nums[i]] = (hash[nums[i]][0] + 1, hash[nums[i]][1] + [i])
    for num in hash.keys():
        search = target - num
        if search == num:
            if hash[num][0] > 1:
                return hash[num][1][:2]
        elif search in hash:
            return [hash[num][1][0], hash[search][1][0]]


def main():
    nums = [2, 4, 11, 3]
    target = 14

    print(two_sum(nums, target))


if __name__ == '__main__':
    main()
