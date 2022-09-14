def Total(Number=10):
    Sum=0
    for C in range(1,Number+1):
        if C%2==0:
            print(Sum,Number)
            continue

        Sum+=C
    return Sum

print(Total(4))
print(Total(7))
print(Total())