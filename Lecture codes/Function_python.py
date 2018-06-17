def f():
    def x(a, b):
        return a+b
    return x
val = f()(3,4)

print(val)