from binary_search.search_in_rotated_sorted_array_ii import search


def test_search():
    assert search([1, 0, 1, 1, 1], 0) is True
    assert search([1, 0, 1, 1, 1], 1) is True
    assert search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert search([2, 5, 6, 0, 0, 1, 2], 3) is False
    assert search([4, 1, 1, 1, 1], 4) is True
    assert search([4, 1, 1, 1, 1], 1) is True
    assert search([4, 1, 1, 1, 1], 2) is False
    assert search([0, 1, 1, 1, 4], 4) is True
    assert search([1, 2, 3, 4, 5], 4) is True
    assert search([5, 1, 2, 3, 4], 4) is True
    assert search([5, 1, 2, 3, 4], 5) is True
    assert search([5, 1, 2, 3, 4], 7) is False
    assert search([5, 1, 2, 3, 4], 0) is False
    assert search([5, 1, 2, 3, 4], 1) is True
    assert search([1, 2], 1) is True
    assert search([1, 2], 2) is True
    assert search([1, 2], 3) is False
    assert search([3, 2], 3) is True
    assert search([3, 2], 2) is True
    assert search([3, 2], 1) is False
    assert search([4, 2, 3], 1) is False
    assert search([4, 2, 3], 3) is True
    assert search([4, 2, 3], 2) is True
    assert search([4, 2, 3], 4) is True
    assert search([4, 2, 3], 6) is False
    assert search([4, 4, 4], 6) is False
    assert search([4, 4, 4], 4) is True
    assert search([4, 1, 4], 4) is True
    assert search([4, 1, 4], 1) is True
    assert search([1, 1, 4], 1) is True
    assert search([1, 1, 4], 4) is True
    assert search([1, 4, 4], 4) is True
    assert search([4, 4, 1], 4) is True
    assert search([4, 4, 1], 1) is True
    assert search([4, 4, 1], 2) is False
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2) is True
