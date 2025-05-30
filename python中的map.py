#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python中的map()函数
这个文件包含了Python中map()函数的详细说明和使用示例
"""

# =============== map()函数基础 ===============

"""
map()函数的基本语法：
map(函数, 可迭代对象)

参数说明：
1. 函数：可以是内置函数、自定义函数或lambda函数
2. 可迭代对象：如列表、元组等

返回值：
- 返回一个map对象
- 需要使用list()转换为列表才能查看结果
"""

# =============== 基本示例 ===============

# 1. 使用内置函数
# 1.1 将字符串列表转换为整数列表
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print("示例1.1 - 字符串转整数：")
print(f"原始字符串列表: {str_numbers}")
print(f"转换后的整数列表: {int_numbers}")

# 1.2 将数字列表转换为字符串列表
numbers = [1, 2, 3, 4, 5]
str_nums = list(map(str, numbers))
print("\n示例1.2 - 整数转字符串：")
print(f"原始数字列表: {numbers}")
print(f"转换后的字符串列表: {str_nums}")

# =============== 使用自定义函数 ===============

# 2. 使用自定义函数
def square(x):
    """计算平方"""
    return x ** 2

def double(x):
    """计算两倍"""
    return x * 2

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
doubled = list(map(double, numbers))

print("\n示例2 - 使用自定义函数：")
print(f"原始数字: {numbers}")
print(f"平方后: {squared}")
print(f"翻倍后: {doubled}")

# =============== 使用lambda函数 ===============

# 3. 使用lambda函数
numbers = [1, 2, 3, 4, 5]
# 使用lambda计算平方
squared = list(map(lambda x: x ** 2, numbers))
# 使用lambda计算立方
cubed = list(map(lambda x: x ** 3, numbers))

print("\n示例3 - 使用lambda函数：")
print(f"原始数字: {numbers}")
print(f"平方后: {squared}")
print(f"立方后: {cubed}")

# =============== 处理多个列表 ===============

# 4. 处理多个列表
list1 = [1, 2, 3]
list2 = [10, 20, 30]
# 对应位置相加
sum_list = list(map(lambda x, y: x + y, list1, list2))
# 对应位置相乘
product_list = list(map(lambda x, y: x * y, list1, list2))

print("\n示例4 - 处理多个列表：")
print(f"列表1: {list1}")
print(f"列表2: {list2}")
print(f"对应位置相加: {sum_list}")
print(f"对应位置相乘: {product_list}")

# =============== 实际应用场景 ===============

# 5. 在输入处理中的应用
print("\n示例5 - 输入处理：")
# 5.1 处理单行输入
print("请输入一组数字（用空格分隔）：")
input_str = input()  # 例如输入：1 2 3 4 5
numbers = list(map(int, input_str.split()))
print(f"转换后的数字列表: {numbers}")

# 5.2 处理多行输入（矩阵）
print("\n请输入矩阵的行数：")
n = int(input())
print(f"请输入{n}行数字，每行用空格分隔：")
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
print(f"输入的矩阵: {matrix}")

# =============== 注意事项 ===============

"""
使用map()函数时需要注意：

1. map()返回的是map对象，需要转换为list才能查看结果
2. 当处理多个列表时，列表长度应该相同
3. 如果列表长度不同，map会以最短的列表长度为准
4. map()是惰性求值的，只有在需要时才会计算
5. 对于大量数据，map()比循环更高效
"""

# 6. 错误处理示例
print("\n示例6 - 错误处理：")
try:
    # 尝试将非数字字符串转换为整数
    str_list = ["1", "2", "abc", "4"]
    numbers = list(map(int, str_list))
except ValueError as e:
    print(f"错误：{e}")
    print("处理方案：使用try-except或先过滤无效数据")

# 7. 性能比较
print("\n示例7 - 性能比较：")
import time

# 使用循环
def using_loop(numbers):
    return [x * 2 for x in numbers]

# 使用map
def using_map(numbers):
    return list(map(lambda x: x * 2, numbers))

# 测试数据
test_data = list(range(1000000))

# 测试循环方法
start_time = time.time()
using_loop(test_data)
loop_time = time.time() - start_time

# 测试map方法
start_time = time.time()
using_map(test_data)
map_time = time.time() - start_time

print(f"循环方法耗时: {loop_time:.4f}秒")
print(f"map方法耗时: {map_time:.4f}秒") 