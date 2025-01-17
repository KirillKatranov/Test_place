

def owner(cat):
    cats = []
    def inner():
        cats.append(cat)
        return cats
    return inner

perem = owner('Tom')
perem1 = owner('Angela')
print(owner('Tom'))
print(owner('Tom')())
print(perem)
print(perem())

print(owner('Angela'))
print(owner('Angela')())
print(perem1)
print(perem1())

