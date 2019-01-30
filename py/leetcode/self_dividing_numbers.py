class Potato:

    def split_num_string(self, num):
        for x in num:
            yield int(x)


    def self_dividing_numbers(self, lower, upper):
        for x in range(lower, upper + 1):
            is_self_dividing = True
            for y in self.split_num_string(x):
                if y == 0:
                    is_self_dividing = False
                elif (x % y) != 0:
                    is_self_dividing = False
            if is_self_dividing:
                yield x


class Potato:

    is_self_dividing = lambda self, num: all(int(num) % 2 == 0 for x in str(num))

num = 23
#is_self_dividing = lambda num: all(int(num) % 2 == 0 for x in str(num))
print(Potato().is_self_dividing(23))
print(Potato().is_self_dividing(22))
