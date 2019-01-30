import pytest


class Solution:

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binx = list(format(x, '064b'))
        biny = list(format(y, '064b'))
        distance = 0
        for x, y in zip(binx, biny):
            if x != y:
                distance += 1
        return distance


@pytest.fixture
def hamming():
    return Solution().hammingDistance


def test_hamming(hamming):
    assert hamming(1, 4) == 2
    assert hamming(680142203, 1111953568) == 19
