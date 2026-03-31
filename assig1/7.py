"""
7. Sum and Average (Until 0)

Write a program that:

Continuously inputs numbers
Stops when 0 is entered
Outputs:
sum
average

Input:
1 2 3 0
Output:
6
2.0
"""
total = 0
cnt = 0
for a in map(int, input().split()):
    if a == 0:
        break
    total += a
    cnt += 1

print(total)
print(total / cnt)