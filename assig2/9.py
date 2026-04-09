"""
Task 9: Remove Duplicates (5 pts)
• input 10 numbers
• remove duplicates using a set
"""

a = list(map(int, input().split()))

a = set(a)

print(*a)
