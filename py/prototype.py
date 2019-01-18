class Prototype:

    def __init__(self, *args, **kwargs):
        self.a = 1

    def clone(self, *args, **kwargs):
        obj = self.__class__()
        obj.__dict__.update(kwargs)
        return obj


a = Prototype()
b = a.clone(b=1)
c = b.clone(c=1)
print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
