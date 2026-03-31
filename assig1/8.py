"""
8. Maximum and Minimum

Write a program that:

Inputs numbers until 0
Outputs:
maximum
minimum

Input:
10 22 1 -5 16 0
Output:
22
-5
"""
mn = float('inf')
mx = 0
for a in map(int,input().split()):
    if a == 0: break
    if a > mx:
        mx = a
    if a < mn:
        mn = a
print(mx)
print(mn)