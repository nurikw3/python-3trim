"""
5. Lucky Number. Write a program that:

Inputs a 6-digit number
Checks if sum of first 3 digits equals last 3 digits

Input:
434065
Output:
Yes
"""

num = input()
f_n = sum([int(i) for i in num[:3]])
s_n = sum([int(i) for i in num[3:]])
f = f_n and s_n

print('Yes' if f else 'No')