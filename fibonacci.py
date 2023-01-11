
def fibonacci(n):
    """Return tuple of the nth, n-1th fibonacci pair."""
    if n <= 1:
        return (n, 0)
    (a, b) = fibonacci(n-1)
    return (a+b, a)


def inefficient_fibonacci(n):
    """Return the nth fibonacci number. This is inefficient due to repeated work in return statement. TODO: More explanation."""
    if n <= 1:
        return n
    return inefficient_fibonacci(n-2) + inefficient_fibonacci(n-1)


def memo_fibonacci(n, memo={}):
    """Compute nth fibonacci using memoization to avoid repeated work.

    Time: O(n)
    """
    if n <= 1:
        return n
    try:
        result = memo[n]
    except KeyError:
        result = memo_fibonacci(n-1, memo) + memo_fibonacci(n-2, memo)
        memo[n] = result
    return result


def iterative_fibonacci(n):
    """Compute fibonacci iteratively. This is the optimal solution.

    Time: O(n)"""
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    return b


if __name__ == '__main__':
    # print(fibonacci(1))
    # print(fibonacci(2))
    # print(fibonacci(3))
    # print(fibonacci(4))

    # print(inefficient_fibonacci(1))
    # print(inefficient_fibonacci(2))
    # print(inefficient_fibonacci(3))
    # print(inefficient_fibonacci(4))

    # print(iterative_fibonacci(1))
    # print(iterative_fibonacci(2))
    # print(iterative_fibonacci(3))
    # print(iterative_fibonacci(4))

    print(memo_fibonacci(1))
    print(memo_fibonacci(2))
    print(memo_fibonacci(3))
    print(memo_fibonacci(4))
