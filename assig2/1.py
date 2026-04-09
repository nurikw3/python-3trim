"""
Task 1: Second Largest Element (10 pts) Write a program that:
• inputs a list of integers
• finds the second largest element
• do NOT use sort()
"""

a = list(map(int, input().split()))

largest = max(a)
second_largest = max([x for x in a if x != largest])
print(second_largest)
