answer = 0
column = 8

while True:
    print("Enter Bit Value:\t")
    b = int(input())
    answer += column * b
    column /= 2
    if column < 1:
        break

print("Decimal value is:\t", answer)