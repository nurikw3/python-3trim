nums = [5, 12, 7, 18, 20]

print(list(map(lambda x: x * x, filter(lambda x: x > 10, nums))))