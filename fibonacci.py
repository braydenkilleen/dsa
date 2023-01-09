
def fibonacci(n):
    """Return tuple of the nth, n-1th fibonacci pair."""
    if n <= 1:
        return (n, 0)
    (a, b) = fibonacci(n-1)
    return (a+b, a)


if __name__ == '__main__':
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
