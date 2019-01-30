def array_parity_sort(nums):
    evens, odds = [], []
    for x in nums:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)
    return sorted(evens) + sorted(odds, reverse=True)


def test_array_parity():
    assert array_parity_sort([3,1,2,4]) == [2, 4, 1, 3]
