def merge(d1, d2):
    return d2.update(d1)

test = {"test": "test"}
test2 = {"test2": "test2"}

test3 = test.update(test2)
test4 = merge(test, test2)

print(test3)
print(test4)
print(z)