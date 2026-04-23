def find_max(*args: int | float) -> int | float:
    mx = args[0]
    for num in args:
        if num > mx:
            mx = num
    return mx

if __name__ == "__main__":
    print(find_max(1, 5, 3, 9, 2))
    print(find_max(-1, -5, -3, -9, -2))
    print(find_max(3.14, 2.71, 1.41))