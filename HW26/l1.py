class Iterator:
    def __init__(self, num: int):
        self.__num = num
        self.__count = 0

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self):
        self.__count += 1
        if self.__count > self.__num:
            raise StopIteration
        return self.__count ** 2


def f_iterator(num: int):
    for i in range(1, num + 1):
        yield i ** 2


num = 5
cl_iter = Iterator(num)
for elem in cl_iter:
    print(elem)
print()

f_iter = f_iterator(num)
for elem in f_iter:
    print(elem)
print()

gen_iter = (x ** 2 for x in range(1, num + 1))
for elem in gen_iter:
    print(elem)
