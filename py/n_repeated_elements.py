def num_repeated(nums):
    repeated = 0
    for x in range(len(nums)):
        a = nums.pop(0)
        if a in nums:
            return a


def test_num_repeated():
    assert num_repeated([8,3,2,3]) == 3
    assert num_repeated([2,1,2,5,3,2]) == 2
    assert num_repeated([1,2,3,3]) == 3
    assert num_repeated([5,1,5,2,5,3,5,4]) == 5
