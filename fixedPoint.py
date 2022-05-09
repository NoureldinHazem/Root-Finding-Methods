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


# getting the x = g(x) expression
def get_gx(function):
    x = sympy.symbols('x')
    function = sympy.sympify(function)
    try:
        degree = sympy.degree(function)
        leading_coeff = sympy.LC(function)
        leading_coeff = sympy.sympify(leading_coeff)
        leading_term = sympy.LT(function) * -1
        leading_term = sympy.sympify(leading_term)
        gx = sympy.Add(function, leading_term)
        gx, rem = sympy.div(gx, leading_coeff)
        gx = sympy.Mul(gx, -1)
        gx = sympy.Pow(gx, 1 / degree)
    except:
        gx = sympy.Add(function, x * x)
        gx = str(function)
        gx = "( " + gx + " ) ^ (1/2)"
        gx = sympy.sympify(gx)

    gx = str(gx)
    gx = gx.replace("**", "^")
    return gx



# fixed point method calculations
def fixedPoint(equation, x0, eps=0.00001, max_iterations=50, flag = 0, gxTxt = ""):
    start_time = time.time()

    if flag:
        gx = gxTxt
    else:
        gx = get_gx(equation)

    i = 1
    convergent = 1
    check_condition = True
    x1_list = []
    x0_list = []
    tolerance_list = []
    while check_condition:
        x1 = f(x0, gx)
        x0_list.append(x0)
        x1_list.append(x1)
        i += 1
        if i > max_iterations:
            convergent = 0
            tolerance = abs(x1 - x0)
            tolerance_list.append(tolerance)
            break
        tolerance = float(abs((x1 - x0)/x1))
        tolerance = round(tolerance, 7)
        tolerance_list.append(tolerance)
        x0 = x1
        check_condition = tolerance > eps
    end_time = time.time()
    elapsed_time = end_time - start_time

    data = []
    for x in range(len(x0_list)):
        row = []
        row.append(x0_list[x])
        row.append(x1_list[x])
        row.append(tolerance_list[x])
        data.append(row)
    data.append(elapsed_time)
    data.append(convergent)
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
    equation = input("F(x) =  ")
    x0 = float(input("Initial guess =  "))
    epsilon = float(input("Tolerance =  "))
    fixedpoint_data = fixedPoint(equation, x0, epsilon)
    convergent = fixedpoint_data[len(fixedpoint_data) - 1]
    fixedpoint_data.pop(len(fixedpoint_data) - 1)
    elapsed_time = fixedpoint_data[len(fixedpoint_data) - 1]
    fixedpoint_data.pop(len(fixedpoint_data) - 1)
    root = fixedpoint_data[len(fixedpoint_data)-1][1]
    precision = fixedpoint_data[len(fixedpoint_data)-1][2]
    iterations = len(fixedpoint_data)
    if convergent == 0:
        print("Function is diverging.\n\n\n")

    print(pandas.DataFrame(fixedpoint_data, index=range(1, iterations+1), columns=["X(i)", "X(i+1)", "Relative Error"]))
    print("\nApproximate root is = %0.8f" % root)
    print("\nElapsed time is %f seconds" % elapsed_time)
    print("\nPrecision is %f\n" % precision)
    plot(equation)
