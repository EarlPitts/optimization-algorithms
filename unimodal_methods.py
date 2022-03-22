def zero(f, a, b, num_of_iter):
    """
    Harmadolos megoldas
    f: objective function
    [a,b]: search interval
    num_of_iter: number of iterations
    """
    ak = a
    bk = b

    for i in range(num_of_iter):
        xl = (2 * ak + bk) / 3 # Lower third
        xh = (ak + 2 * bk) / 3 # Higher third
        # We can drop the left/right third (no minimizer there)
        if f(xl) < f(xh):
            bk = xh
        else:
            ak = xl

    return (ak + bk) / 2

def newton(df,ddf,x0,num_of_iter):
    """
    df: derivative
    ddf: second derivative
    x0: starting point
    num_of_iter: number of iterations
    """

    x = x0
    for i in range(num_of_iter):
        x = x - df(x) / ddf(x)
    return x
