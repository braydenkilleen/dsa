def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)


def factorial2(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans


if __name__ == '__main__':
    assert factorial(4) == 24

    assert factorial2(4) == 24
