def zigzag(n):
    for i in range(n):
        print(' ' * i + '*' + ' ' * (n - i - 1))

zigzag(5)
