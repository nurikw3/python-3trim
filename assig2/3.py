"""
Task 3: Split Even and Odd (10 pts)
Write a program that:
• inputs a list
• creates two lists:
o even numbers
o odd numbers
"""

a = list(map(int, input().split()))

a_even = [x for x in a if x % 2 == 0]
a_odd = [x for x in a if x % 2 != 0]

print(a_even)
print(a_odd)
