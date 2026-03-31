"""
1. Write a program that: Inputs two numbers a and b
Outputs how much greater one is than the other

Input:
56
50
Output:
6
"""

a = int(input())
b = int(input())

if a > b:
    print(a-b)
elif a < b:
    print(b-a)
else:
    print(a-b)