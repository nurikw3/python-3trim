"""
9. Sum of Odd Numbers

Write a program that:

Inputs numbers until 0
Outputs sum of odd numbers only

Input:
1 2 3 4 5 0
Output:
9
"""

s = 0
for a in map(int,input().split()):
    if a == 0: break
    if a % 2 != 0:
        s+=a
print(s)
