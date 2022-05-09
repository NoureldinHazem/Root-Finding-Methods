import pandas
import time
import matplotlib.pyplot as plt
import numpy as np
import sympy


# function calculating f(x) for any value of x
def f(x_val, function):
    x = sympy.symbols('x')
    function = sympy.sympify(function)
    result = function.evalf(8, subs={x: x_val})
    return result

def secant(function, xold, xcurrent, eps, max_iterations):

    start_time = time.time()
    i = 0

    # to check that  the smaller number in xold and the bigger in the xcurrent and if not change them
    if xold > xcurrent:
        temp = xcurrent
        xcurrent = xold
        xold = temp

    xold_list = []                 # list of x(i-1) elements
    xcurrent_list = []             # list of x(i) elements
    xnew_list = []                 # list of x(i+1) elements
    fxold_list = []                # list of f(X(i-1)) elements
    fxcurrent_list = []            # list of f(X(i)) elements
    error_list = []                # list of error elements

    while i < max_iterations:
        xold = round(xold, 6)               # rounding x(i-1)
        xcurrent = round(xcurrent,6)        # rounding x(i)
        xold_list.append(xold)
        xcurrent_list.append(xcurrent)

        fxold = f(xold, function)           # calculating fx(i-1)
        fxcurrent = f(xcurrent, function)   # calculating fx(i)
        fxold = round(fxold, 6)             # rounding fx(i-1)
        fxcurrent = round(fxcurrent, 6)     # rounding fx(i-1)
        fxold_list.append(fxold)
        fxcurrent_list.append(fxcurrent)

        xnew = xcurrent - (fxcurrent * (xold - xcurrent)) / (fxold - fxcurrent)     # calculating x(i+1)
        xnew = round(xnew, 6)                # rounding x(i+1)
        xnew_list.append(xnew)
        fxnew = f(xnew, function)             # calculating fx(i+1)

        xold = xcurrent
        xcurrent = xnew

        error = float(abs((xnew_list[i] - xcurrent_list[i])/xnew_list[i]))       # calculating error
        error = round(error, 6)                                             # rounding error
        error_list.append(error)
        i += 1

        #checking stop condition
        if error < eps or fxnew == 0:
            break

    end_time = time.time()
    elapsed_time = end_time - start_time
    # returning each iteration details in a row of a 2d list to print it using dataframe
    data = []
    for x in range(len(xold_list)):
        row = []
        row.append(xold_list[x])
        row.append(xcurrent_list[x])
        row.append(fxold_list[x])
        row.append(fxcurrent_list[x])
        row.append(xnew_list[x])
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

        x0 = float(input("Initial guess =  "))
        x1 = float(input("Second guess =  "))

        epsilon = float(input("Epsilon = "))
        max_iterations = int(input("Maximum Iterations = "))
        secant_data = secant(equation, x0, x1, epsilon, max_iterations)
        elapsed_time = secant_data[len(secant_data) - 1]
        secant_data.pop(len(secant_data) - 1)
        root = secant_data[len(secant_data) - 1][4]
        precision = secant_data[len(secant_data) - 1][5]
        iterations = len(secant_data)

        print(pandas.DataFrame(secant_data, index=range(1, iterations + 1), columns=["X(i-1)", "X(i)",  "F(x(i-1))", "F(x(i))","X(i+1)", "Relative Error"]))
        print("\nApproximate root is = %f" % root)
        print("\nElapsed time is %f seconds" % elapsed_time)
        print("\nPrecision is %f" % precision)
        print("\nNumber of iterations = %d \n" % iterations)
        plot(equation)