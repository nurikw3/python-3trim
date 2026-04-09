"""
15. Intersection of multiple lists
Given:
L1 = [1,2,3,4]
L2 = [2,3,5]
L3 = [2,3,6]
Find common elements in all lists.
"""

L1 = [1, 2, 3, 4]
L2 = [2, 3, 5]
L3 = [2, 3, 6]

print(*set(L1) & set(L2) & set(L3))
