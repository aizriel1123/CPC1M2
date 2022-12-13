dec = int(input("Enter a decimal integer: "))
print("Quotient Remainder Octal")

oct = 0
i = 1
num = ""

while dec != 0:
    dec = int(dec)

    remainder = dec % 8
    dec //= 8
    oct = oct + remainder * i
    i *= 10
    num = str(remainder) + num

print("%5d%8d%12s" % (dec, remainder, num),'\n The octal representation is ', oct)

