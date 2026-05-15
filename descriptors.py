class D:
    def __get__(self, obj, objtype=None):
        return "descriptor"

    def __set__(self, obj, value):
        print("SET", value)


class Test:
    x = D()

t = Test()
t.__dict__['x'] = 123

print(t.x)
