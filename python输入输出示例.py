#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python输入输出示例
这个文件包含了Python中常用的输入输出操作示例
"""

# 1. 基本的输出操作
print("Hello, World!")  # 最简单的输出
print("你好，世界！")    # 支持中文输出

# 2. 格式化输出
name = "小明"
age = 18
print("我叫{}，今年{}岁".format(name, age))  # 使用format方法
print(f"我叫{name}，今年{age}岁")  # 使用f-string（Python 3.6+）

# 3. 基本的输入操作
user_input = input("请输入你的名字：")  # 获取用户输入
print(f"你好，{user_input}！")

# 4. 输入数字
try:
    number = int(input("请输入一个数字："))
    print(f"你输入的数字是：{number}")
except ValueError:
    print("输入错误，请输入有效的数字！")

# 5. 多行输入输出
print("""这是一个
多行文本
输出示例""")

# 6. 使用print的end参数
print("这行末尾", end="")
print("没有换行")

# 7. 使用print的sep参数
print("Python", "很", "有趣", sep="-")  # 输出：Python-很-有趣 

# =============== 输出格式示例 ===============

# 8. 数字格式化输出
pi = 3.1415926
print(f"保留2位小数：{pi:.2f}")  # 输出：3.14
print(f"保留3位小数：{pi:.3f}")  # 输出：3.142
print(f"科学计数法：{pi:.2e}")  # 输出：3.14e+00

# 9. 对齐输出
text = "Python"
print(f"左对齐：{text:<10}")  # 输出：Python    
print(f"右对齐：{text:>10}")  # 输出：    Python
print(f"居中对齐：{text:^10}")  # 输出：  Python  

# 10. 填充字符
print(f"用*填充：{text:*<10}")  # 输出：Python****
print(f"用#填充：{text:#>10}")  # 输出：####Python
print(f"用-填充：{text:-^10}")  # 输出：--Python--

# 11. 数字格式化
number = 12345
print(f"二进制：{number:b}")  # 输出：11000000111001
print(f"八进制：{number:o}")  # 输出：30071
print(f"十六进制：{number:x}")  # 输出：3039
print(f"带前缀的十六进制：{number:#x}")  # 输出：0x3039

# 12. 千位分隔符
big_number = 1234567
print(f"带千位分隔符：{big_number:,}")  # 输出：1,234,567

# 13. 百分比格式
percentage = 0.85
print(f"百分比：{percentage:.1%}")  # 输出：85.0%

# 14. 格式化字符串的多种方式
name = "小明"
age = 18
score = 95.5
# 方式1：使用 %
print("姓名：%s，年龄：%d，分数：%.1f" % (name, age, score))
# 方式2：使用 format
print("姓名：{}，年龄：{}，分数：{:.1f}".format(name, age, score))
# 方式3：使用 f-string
print(f"姓名：{name}，年龄：{age}，分数：{score:.1f}")

# 15. 格式化输出表格
print("\n学生成绩表：")
print(f"{'姓名':<10}{'年龄':<8}{'分数':<8}")
print("-" * 26)
print(f"{'小明':<10}{18:<8}{95.5:<8.1f}")
print(f"{'小红':<10}{17:<8}{98.0:<8.1f}")
print(f"{'小张':<10}{18:<8}{92.5:<8.1f}")

# =============== 牛客网算法题常见输入输出示例 ===============

# 16. 单行输入一个整数
n = int(input())

# 17. 单行输入多个整数
a, b = map(int, input().split())

# 18. 输入一行字符串
s = input().strip()

# 19. 输入一行多个字符串
str_list = input().split()

# 20. 输入多行数据（已知行数）
n = int(input())  # 第一行输入行数
for _ in range(n):
    line = input().strip()
    # 处理每行数据

# 21. 输入多行数据（未知行数，直到输入结束）
while True:
    try:
        line = input().strip()
        if not line:  # 如果输入空行，退出循环
            break
        # 处理每行数据
    except EOFError:
        break

# 22. 输入二维数组（已知行数和列数）
n, m = map(int, input().split())  # 输入行数和列数
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# 23. 输入多组测试用例
while True:
    try:
        n = int(input())
        # 处理每组测试用例
    except EOFError:
        break

# 24. 输入带空格的字符串并转换为列表
arr = list(map(int, input().split()))

# 25. 输入多行，每行包含多个数字
n = int(input())  # 第一行输入行数
for _ in range(n):
    nums = list(map(int, input().split()))
    # 处理每行数据

# 26. 输入多行，每行一个数字
n = int(input())  # 第一行输入行数
for _ in range(n):
    num = int(input())
    # 处理每个数字