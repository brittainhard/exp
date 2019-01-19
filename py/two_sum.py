def two_sums(nums, target):
    for x in nums:
        current = nums.pop()
        for y in nums:
            if x + y == target:
                return [nums.index(x), nums.index(y)]

print(two_sums([3, 3], 6))
