# 运算

a = 2
a**=2
a//=3
print(a)


print(4>=2)
print(3.0 == 3)
print('abc' == 'abc')
# and 运算
# 短路运算： 第一位是true 才会看 看后面
result = 1 and 'abc'
print(result)
result = 1 and print("短路运算！") # 返回结果是none, 但是会输出
print("'1' and print(\"短路运算！\") = %s"%result)
result = 0 and 1 and 3
print("0 and 1 = %s" %result)
r2 = 1 or 0
r3 = not 0
print(r2)
print(r3)

print("-"*20)
# or 运算
# 短路运算：第一位是 true 后面直接不看
result = True or False
print(result)

print("="*20)
# not 运算

print(not 1) # False
print(not '') # True
print(not 'a') # False

print("-"*20)
# 优先级

a = 1
b = 2
c = 3
print(a is not b)
print(a is c)

print('hi' in 'hillo')