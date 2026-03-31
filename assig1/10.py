"""
10. All-in-One Analyzer

Write ONE program that:

Inputs numbers until 0
Outputs:
sum
average
min
max
sum of odd numbers

Input:
1 2 3 4 5 0
Output:
Sum: 15
Average: 3.0
Min: 1
Max: 5
Odd Sum: 9
"""

s_odd = sum_total = mx = cnt = 0
mn = float('inf')
for a in map(int,input().split()):
    if a == 0: break
    if a % 2 != 0:
        s_odd+=a
    sum_total+=a
    cnt+=1
    if mn > a:
        mn = a
    if mx < a:
        mx = a
print(f"Sum: {sum_total}")
print(f"Average: {sum_total / cnt:.1f}")
print(f"Min: {mn}")
print(f"Max: {mx}")
print(f"Odd Sum: {s_odd}")