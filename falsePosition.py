import math
import pandas
import time
import numpy as np
import sympy
import matplotlib.pyplot as plt
import sys


# function calculating f(x) for any value of x
# reserved functions is a dictionary for any known functions input as strings
def f(x_val, function):
    x = sympy.symbols('x')
    function = sympy.sympify(function)
    result = function.evalf(8, subs={x: x_val})
    result = round(result, 6)                            # rounding the result to only 6 decimals places
    return result

# False Position method calculations
def falseposition(function, xlow, xupper, eps, max_iterations):

        start_time = time.time()
        fxl = f(xlow, function)          # calculate x lower function
        fxu = f(xupper, function)        # calculate x upper function
        xr = 0

        if fxl*fxu > 0:                  # checking base condition if False position is valid
            print("False Position not valid")
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

        while i < iterations:
            xlower_list.append(xlow)
            xupper_list.append(xupper)
            xr = (xlow*fxu - xupper*fxl) / (fxu - fxl)
            xr = round(xr, 6)           # rounding xr to only 6 decimals places
            fxr = f(xr, function)
            xr_list.append(xr)
            fxr_list.append(fxr)
            if fxr == 0:             # when x is the root
                break
            if fxr * fxl > 0:       # when x root is the same sign as x lower
                xlow = xr
            else:                   # when x root is the same sign as x upper
                xupper = xr

            if i == 0 and i != iterations:
                    error_list.append(np.nan)
                    i += 1
                    continue
            error = abs((xr_list[i] - xr_list[i - 1]) / xr_list[i])
            error_list.append(error)
            i += 1

            if error < eps:
                break

        end_time = time.time()
        elapsed_time = end_time - start_time

        # returning each iteration details in a row of a 2d list to print it using dataframe
        data = []
        for x in range(iterations):
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
        equation = input("Enter function :\n")
        equation = equation.split("=", 1)[0]
        xl = float(input("Xl = "))
        xu = float(input("Xu = "))
        epsilon = float(input("Epsilon = "))
        max_iterations = int(input("Maximum Iterations = "))
        falsePosition_data = falseposition(equation, xl, xu, epsilon, max_iterations)
        elapsed_time = falsePosition_data[len(falsePosition_data) - 1]
        falsePosition_data.pop(len(falsePosition_data) - 1)
        root = falsePosition_data[len(falsePosition_data) - 1][2]
        precision = falsePosition_data[len(falsePosition_data) - 1][4]
        iterations = len(falsePosition_data)

        print(pandas.DataFrame(falsePosition_data, index=range(1, iterations + 1), columns=["X lower", "X upper", "X root", "F(x root)", "Tolerance"]))
        print("\nApproximate root is = %f" % root)
        print("\nElapsed time is %f seconds" % elapsed_time)
        print("\nPrecision is %f" % precision)
        print("\nNumber of iterations = %d \n" % iterations)
        plot(equation)