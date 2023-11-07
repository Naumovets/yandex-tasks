# Easy
# guess number higher or lower
# https://leetcode.com/problems/guess-number-higher-or-lower/

def guess(index):
    """
    The guess API is already defined for you.
    @param num, your guess
    @return -1 if num is higher than the picked number
             1 if num is lower than the picked number
             otherwise return 0
    """
    ...


def guess_number(n):
    """
    :type n: int
    :rtype: int
    """
    start = 0
    end = n
    current = (start + end) // 2
    while True:
        result = guess(current)
        if result == 0:
            return current
        if result == 1:
            start = current + 1
        else:
            end = current - 1
        current = (start + end) // 2


def main():
    ...


if __name__ == '__main__':
    main()