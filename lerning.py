def quick_merge(n):
    result = []
    a = []
    for i in range(n):
        a = [int(c) for c in input().split()]
        result = result + a
        result.sort()
    return (result)
numbers1 = int(input())
print(*(quick_merge(numbers1)))

