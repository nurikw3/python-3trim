"""
6. Tourist Speed Comparison

Write a program that:

Inputs: D, t1, t2
Tourist walks:
15 km in t1 hours (before noon)
remaining distance in t2 hours (after noon)
Output when speed was higher

Input:
21 5 3
Output:
Before
"""
D, t1, t2 = map(int, input().split())
print("Before" if t1 >= t2 else "After")