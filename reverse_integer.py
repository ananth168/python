def reverse_integer(num):
    sum = 0
    sign = 1

    if num < 0:
        sign = -1
        num = num * -1

    while num > 0:
        rem = num % 10
        sum = sum * 10 + rem
        num = num // 10

    return sign*sum

integer = int(input("enter a integer: "))
result = reverse_integer(integer)
print('reversed integer is: ', result)