import heapq
#1 задание
def elem(spis):
    sum = 0
    for i in spis:
        sum = sum + i
    return sum

print(elem([1,3,5,7,9]))

#2 Задание


def max_2(a, b, c, d):
    return min(a, b, c, d)

print(max_2([3, 10, 22, 5]))

#3 Задание

def z_3(prost):
    a = 0
    for i in prost:
        if i % 2 == 0:
            continue
        else:
            a += 1
    return a
print("простые числа", z_3(prost=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#4 задание

def z_4(num, target):
    a = 0
    i = 0
    while i < len(num):
        if num[i] == target:
            num.pop(i)
            a += 1
        else:
            i += 1
    return a

num = [4, 5, 6, 7, 8, 9, 10]
target = 5
print(z_4(num, target))
print(num)

#5 задание

def z_5(list1, list2):
    return list(heapq.merge(list1, list2))


list1 = [1, 3, 5]
list2 = [2, 4, 6]
z_5 = z_5(list1, list2)
print(z_5)

#6 задание

def z_6(nums, power):
   return [num ** power for num in nums]


nums = [1, 2, 3, 4, 5]
power = 2
result = z_6(nums, power)
print(result)