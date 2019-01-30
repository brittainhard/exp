import heapq


class Potato:

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heapq.heapify(nums)
        total = 0
        for x in range(0, len(nums), 2):
            total += min(nums[x], nums[x + 1])
        return total



def test_min_pairs():
    assert Potato().arrayPairSum([1, 4, 3, 2]) == 4
    assert Potato().arrayPairSum([1, 4, 3, 2, 6, 5]) == 9
