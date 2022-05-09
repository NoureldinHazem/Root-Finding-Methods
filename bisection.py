import math
import pandas
import time
import matplotlib.pyplot as plt
import numpy as np
import sympy
import sys

# function calculating f(x) for any value of x
def f(x_val, function):
    x = sympy.symbols('x')
    function = sympy.sympify(function)
    result = function.evalf(8, subs={x: x_val})
    return result


# bisection method calculations
def bisection(funtion, xlow, xupper, eps, max_iterations):

    start_time = time.time()
    fxl = f(xlow, funtion)              # calc x lower
    fxu = f(xupper, funtion)            # calc x upper
    xr = 0
    error = np.inf

    if fxl*fxu > 0:
        print("Bisection not valid ")       # checking base condition if bisection is valid
        return -1

    # calculating number of iteration which is the minimum of the ( max iterations argument ) and the calculated iterations
    iterations = min(int(math.ceil(math.log((xupper - xlow) / eps, 2))), max_iterations)
    i = 0

    # a list for each output type
    xlower_list = []
    xupper_list = []
    xr_list = []
    fxr_list = []
    error_list = []

    while i < iterations and error > eps:
        xlower_list.append(xlow)
        xupper_list.append(xupper)
        xr = (xlow + xupper) / 2
        fxr = f(xr, funtion)
        xr_list.append(xr)
        fxr_list.append(fxr)
        if fxr * fxl > 0:           # when x root is the same sign as x lower
            xlow = xr
        elif fxr * fxu > 0:         # when x root is the same sign as x upper
            xupper = xr
        else:
            exit(-2)

        if i == 0 and i != iterations:
            error_list.append(np.nan)
            i += 1
            continue
        error = abs( (xr_list[i] - xr_list[i-1]) / xr_list[i] )
        error_list.append(error)
        i += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    # returning each iteration details in a row of a 2d list to print it using dataframe
    data = []
    for x in range(i):
        row = []
        row.append(xlower_list[x])
        row.append(xupper_list[x])
        row.append(xr_list[x])
        row.append(fxr_list[x])
        row.append(error_list[x])
        data.append(row)
    data.append(elapsed_time)
    return data

# function to plot the equation
def plot(equation):
    # setting the x - coordinates
    x = np.arange(-10, 10, 0.1)
    # setting the corresponding y - coordinates
    y = []
    i = 0
    while i < 200:
        ans = f(x[i], equation)
        y.append(ans)
        i += 1

    # plotting the points
    plt.plot(x, y)
    plt.grid(True, which='both')

    # function to show the plot
    plt.show()

if __name__ == "__main__":
    epsilon = 0.000001
    max_iterations = 50
    equation = input("Enter function :\n\n")
    equation = equation.split("=", 1)[0]
    xl = float(input("Xl = "))
    xu = float(input("Xu = "))
    epsilon = float(input("Epsilon = "))
    max_iterations = int(input("Maximum Iterations = "))
    Bisection_data = bisection(equation, xl, xu, epsilon, max_iterations)
    elapsed_time = Bisection_data[len(Bisection_data)-1]
    Bisection_data.pop(len(Bisection_data)-1)
    root = Bisection_data[len(Bisection_data)-1][2]
    precision = Bisection_data[len(Bisection_data)-1][4]
    iterations = len(Bisection_data)

    print(pandas.DataFrame(Bisection_data, index=range(1, iterations+1), columns=["X lower", "X upper", "X root", "F(x root)", "Relative error"]))
    print("\nApproximate root is = %f" % root)
    print("\nElapsed time is %f seconds" % elapsed_time)
    print("\nPrecision is %f\n" % precision)
    plot(equation)