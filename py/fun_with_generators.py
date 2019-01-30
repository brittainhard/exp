def evens_generate(nums):
    for x in nums:
        if x % 2 == 0:
            yield x


a = evens_generate([1, 2, 3, 4, 5, 6])
print(list(a))
