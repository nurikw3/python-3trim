"""
Task 8: Max Tuple by Sum (5 pts)
t = ((1,5), (2,3), (7,1))
• find tuple with largest sum
"""

t = ((1, 5), (2, 3), (7, 1))

for i in t:
    if i[0] + i[1] > t[0][0] + t[0][1]:
        print(i)
