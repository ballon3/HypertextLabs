digits = 0
digit = 0
v = 7
total = 0
flag = 'true'
decimal = input("Please enter an 8 bit binary number:")
for x in decimal:
    try:
        digit = int(x)
    except: 
        flag = 'error'
        break
    if digit < 0 or digit > 1:
        print("Not Binary")
        flag = 'error1'
        break
    else:
            digits = digits + 1

if digits != 8:
        print("Not 8 bit")
        flag = 'error2'
for x in decimal:
    digit = int(x)
    total = digit*(2**v) + total
    v = v - 1
#decimal += digit*(2**7)
#decimal += digit*(2**6)
#decimal += digit*(2**5)
#decimal += digit*(2**4)
#decimal += digit*(2**3)
#decimal += digit*(2**2)
#decimal += digit*(2**1)
#decimal += digit*(2**0)
#printing
if flag == 'true':
    print("Your decimal number is ", total, "Congratulations") 
else:
    print("Error, Not a valid 8 bit binary") 
