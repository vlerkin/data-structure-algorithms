import timeit

print(-7 // 2)
print(int(-7 / 2))

print(3//2 == int(3/2))

b = [1, 2, 3, 4, 5]
b_copy = b.copy()
d = b[:]
d.extend([555, 666, 777])
d.append([555, 666, 777])
b[2:2] = [100, 101, 102]
c = 2
c *= 2
print(b)
print(c)
print(d)
print(b_copy)


def append(alist, iterable):
    for item in iterable:
        alist.append(item)


def extend(alist, iterable):
    alist.extend(iterable)


print(min(timeit.repeat(lambda: append([], "abcdefghijklmnopqrstuvwxyz"))))

print(min(timeit.repeat(lambda: extend([], "abcdefghijklmnopqrstuvwxyz"))))

def append_one(a_list, element):
    a_list.append(element)

def extend_one(a_list, element):
    """creating a new list is semantically the most direct
    way to create an iterable to give to extend"""
    a_list.extend([element])

print(min(timeit.repeat(lambda: append_one([], 0))))
print(min(timeit.repeat(lambda: extend_one([], 0))))