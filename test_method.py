import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import unimodal_methods as um
import line_search_methods as ls
import samples as s

def test_zero(f):
    fig, ax = plt.subplots()

    # Plot the objective function
    X = np.linspace(0, 10, 100)
    Y = f(X)
    ax.plot(X, Y)

    # Get the guesses for each iteration
    x = []
    for i in range(10):
        x.append(um.zero(f, 0, 10, i))

    x = np.array(x)

    # Plot the guesses
    ax.scatter(x, f(x), color='red')

    plt.show()

def test_newton(f, df, ddf):
    fig, ax = plt.subplots()

    # Plot the objective function
    X = np.linspace(0, 10, 100)
    Y = f(X)
    ax.plot(X, Y, color='orange')

    # Get the guesses for each iteration
    x = []
    for i in range(10):
        x.append(um.newton(df, ddf, 5, i))

    x = np.array(x)

    # Plot the guesses
    ax.scatter(x, f(x), color='purple')

    plt.show()

def test_armijo_basic(f, df):
    fig, ax = plt.subplots()

    # Plot the objective function
    X = np.linspace(0, 10, 100)
    Y = f(X)
    ax.plot(X, Y, color='orange')

    # Get the guesses for each iteration
    x = []
    for i in range(10):
        x.append(ls.armijo_basic(f, df, 7, i))

    x = np.array(x)

    # Plot the guesses
    ax.scatter(x, f(x), color='purple')

    plt.show()

# test_zero(s.f3)
# test_newton(s.f1, s.df1, s.ddf1)
test_armijo_basic(s.f1, s.df1)
