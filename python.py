def fibonacci(n):
    """
    Generates the Fibonacci series up to the nth term.
    
    Args:
    n (int): Number of terms in the Fibonacci series.
    
    Returns:
    list: A list containing the Fibonacci series.
    """
    a, b = 0, 1
    fib_sequence = []
    
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    
    return fib_sequence


if __name__ == "__main__":
    # Example usage
    terms = 10
    fib_series = fibonacci(terms)
    print(f"The first {terms} terms of the Fibonacci series are: {fib_series}")
