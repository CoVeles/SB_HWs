class QHofstadter:
    def __init__(self, sequence):
        if sequence is None:
            sequence = [1, 1]
        self.sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        try:
            # Т.К. номер элемента на 1 меньше его реального места,
            # то n в функцию передаем как (n - 1)
            n = (len(self.sequence))
            # получим следующий элемент
            member = (self.sequence[n - self.sequence[n - 1]]
                      + self.sequence[n - self.sequence[n - 2]])
            # и добавим его в последовательность
            self.sequence.append(member)
            return member
        except IndexError:
            raise StopIteration()


Q = QHofstadter([1, 1])

try:
    for _ in range(300):
        print(next(Q), end=' ')
except StopIteration:
    print('Последовательность умерла!')

print()
Q = QHofstadter([3, 3])

try:
    for _ in range(20):
        print(next(Q), end=' ')
except StopIteration:
    print('Последовательность умерла!')
