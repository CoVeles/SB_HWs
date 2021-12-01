list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]


def search_generator(to_find: int):
    for x in list_1:
        for y in list_2:
            result = x * y
            yield f'{x} * {y} = {result}'
            if result == to_find:
                print('Найдено!!!')
                return


to_find = 56
search = search_generator(to_find)
for attempt in search:
    print(attempt)
    
