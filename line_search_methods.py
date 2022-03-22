def armijo_basic(f, df, x0, num_of_iter):
    """
    Linesearch on descent direction
    Each iteration runs until the Armijo condition is satisfied
    f: objective function
    df: derivative
    x0: starting point
    """
    init_alpha = 1 # Initial step length
    rho = 0.5 # Step length multiplier
    c = 0.2 # Armijo condition modifier
    x = 0

    for i in range(num_of_iter):
        breakpoint()
        alpha = init_alpha
        f0 = f(x0)
        df0 = df(x0)
        if df0 > 0:
            alpha = -alpha # Selecting descent direction

        x = x0 + alpha
        fx = f(x)

        while fx < f0 + x * alpha * df0:
            alpha = alpha / rho
            x = x0 + alpha
            fx = f(x)
        while fx > f0 + c * alpha * df0:
            alpha = rho * alpha
            x = x0 + alpha
            fx = f(x)

        x0 = x # Update starting point for next iteration

    return x
