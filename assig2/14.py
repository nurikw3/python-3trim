"""
Task 14: Remove Non-Unique Elements (10 pts)
[1,2,2,3,4,4,5]
• output only elements that appear once:
[1,3,5]
"""

from collections import Counter

a = list(map(int, input().split()))

# print(*[i for i in a if Counter(a)[i] == 1])
for i in a:
    if a.count(i) == 1:
        print(i, end=" ")
