def analyze_number[T : int | float](num: T) -> tuple[str, str, str]:
    if num % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    
    if num > 0:
        nn = "positive "
    elif num < 0:
        nn = "negative " 
    else:
        nn = "zero"
    
    return (parity, nn, str(num * num))

if __name__ == "__main__":
    print(analyze_number(5))
    print(analyze_number(3.14))
    print(analyze_number(-2))
    print(analyze_number(4))
