"""
2. Even Numbers. Write a program that: Inputs integer n
Outputs all even numbers from 0 to n (inclusive)
Input:
8
Output:
0 2 4 6 8
"""

for i in range(0,int(input())+1,2):
    print(i,end=' ')