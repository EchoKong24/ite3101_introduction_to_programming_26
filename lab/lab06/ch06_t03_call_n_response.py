def square(n: float) -> float:
    """Returns the square of a number."""
    squared = n ** 2
    print("%d squared is %d." % (n, squared))
    return squared


# Call the function with 10.
square(10)