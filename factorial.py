def factorial_rec(num):
    if num <= 2:
        return num
    else:
        return num + factorial_rec(num-1)


if __name__ == '__main__':
    print(factorial_rec(4))