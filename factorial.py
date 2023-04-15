def factorial_rec(num):
    if num < 2:
        return num
    else:
        return num * factorial_rec(num - 1)


def factorial_iter(num):
    fact = 1
    if num < 2:
        return num
    while num > 1:
        fact *= num
        num -= 1
    return fact


if __name__ == '__main__':
    print(factorial_rec(4))
    print(factorial_iter(6))
