
def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)

def count_last_digit_zero(num):
    count = 0
    while int(num) % 10 == 0:
        count += 1
        num //= 10
    return count

x = 10
fac = factorial(x)
print(count_last_digit_zero(fac))