def fact_func(n):
    if n <= 1:
        return 1
    return n * fact_func(n-1)
