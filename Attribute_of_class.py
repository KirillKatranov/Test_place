class A:
    atr = 1
    def __init__(self):
        pass

a = A()
b = A()
print(a.atr)
a.atr = 5
print(a.atr)
print(b.atr)
print(A.atr)
A.atr = 7

print(A.atr)
print(b.atr) 
b.atr = 4
print(b.atr)
A.atr = 8
print(b.atr)
