"""
Task 2: Rotate List (10 pts)
Given a list:
L = [1, 2, 3, 4, 5]
• rotate it right by 1
• print result
"""

L = list(map(int, input().split()))
L.insert(0, L.pop())
print(L)
