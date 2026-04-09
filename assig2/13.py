"""
Task 13: Pair Sum (10 pts)
L = [2,7,11,15]
target = 9
• find two numbers whose sum = target
"""

L = [2, 7, 11, 15]
target = 9

l, r = 0, len(L) - 1

while l < r:
    if L[l] + L[r] == target:
        print(L[l], L[r])
        break
    elif L[l] + L[r] < target:
        l += 1
    else:
        r -= 1
