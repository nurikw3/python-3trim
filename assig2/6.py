"""
Task 6: Convert & Modify (5 pts)
• convert tuple → list
• add an element
• convert back to tuple
"""

t = (1, 2, 3, 4, 5)

a = list(t)
a.append(int(input()))
t = tuple(a)
print(t)
