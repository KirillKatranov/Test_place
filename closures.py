# Внутренняя функция, которая возвращается из внешней и имеет доступ к глобальному скоупу
# Замыкания не пересекаются, а каждый раз создают новый объект функции и запоминают состояние

def owner():
    cats = []
    def inner(cat):
        cats.append(cat)
        return cats
    return inner

perem = owner()
perem1 = owner()
print(owner())
print(owner()('Tom'))
print(perem)
print(perem('Tom'))
print(perem("Jack"))

print(owner()('Angela'))
print(perem1)
print(perem1('Angela'))
print(perem1('Alice'))

