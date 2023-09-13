def merge(list1, list2):
    a = []
    a = list1 + list2
    a.sort()
    return (a)

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))