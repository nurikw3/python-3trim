"""
3. Reverse Order. Write a program that: Inputs integer n
Outputs numbers from n down to 0
Input:
5
Output:
5 4 3 2 1 0
"""

for i in range(int(input()), -1,-1):
    print(i,end=' ')