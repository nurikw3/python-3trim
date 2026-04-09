"""
L = [[1,2], [3,4], [5]]
• output a flat list:
[1,2,3,4,5]
"""

L = [[1, 2], [3, 4], [5]]

for i in L:
    for j in i:
        print(j, end=" ")
