num = int(input("Enter a string of octal digits:"))


def octaldeci(num):
    total = 0
    i = 0
    while num != 0:
        remainder = num % 10
        total += remainder * pow(8, i)
        i = i + 1
        num = int(num / 10)
    return total


ans = octaldeci(num)
print("The integer value is", ans)
