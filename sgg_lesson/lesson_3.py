""""
content:
1. 选择语句
2. match 相当于switch case
3. 循环语句
    while
    for
"""
import math

score = 92
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")

x = 'hello world'
match x:
    case 'hello world':
        print("1")
    case 10:
        print("10")
    case _:
        print("not a number")

# 判断润年

year = 2000
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("a run year")
else:
    print("not a run year")

# while 循环
n = 1
while n < 5:
    n += 1
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


# for
# 阶乘 factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 前n项阶乘的和
def sumFactorial(n):
    if n <= 0:
        return -1
    result = 0
    for i in range(1, n + 1):
        result += factorial(i)
    return result

print(sumFactorial(3))

# 判断 质数
def primeNum(n):
    if n < 0:
        return None
    if 0<= n < 2:
        return True
    for i  in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print(primeNum(-1))


# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d x %d = %d\t" % (j, i, i * j), end='')
#     print("\n")

# 输出问题

import time
for i in range(5):
    print(i, end='')   # 没有 flush，可能等循环结束后一次性输出 "01234"
    print(i, end='', flush=True)
    time.sleep(1)      # 每个数字延迟1秒，但终端可能一直没显示，最后突然全出来