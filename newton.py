import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy 
import time

# function calculating f(x) for any value of x
def f(x_val, function):
    x = sympy.symbols('x')
    function = sympy.sympify(function)
    result = function.evalf(8, subs={x: x_val})
    return result




def newtenraphson(equation,x_i=0,eps=0.00001, maxItr=50):
    start_time = time.time()
    x = sympy.symbols('x')
    function = sympy.sympify(equation)
    diff = function.diff()
    itr = 0

    x0_list =[]              # list of x(i) elements     
    x1_list = []             # list of x(i1) elements
    tolerance_list = []      # list of tolerance elements


    while True:
        fx = f(x_i,equation)     # calculating fx(i)
        dfx = f(x_i,diff)        # calculating dfx(i)
        x_i1 = x_i - fx/dfx      # calculating X(i1)
        x0_list.append(x_i)
        x1_list.append(x_i1)


        tolerance = float(abs((x_i1 - x_i)/x_i1))  # calculating error
        tolerance = round(tolerance, 7)      # rounding error
        tolerance_list.append(tolerance)
        x_i = x_i1
        itr +=1

         #stop condition 
        if eps > tolerance :
            break
        if itr == maxItr:
            break


    end_time = time.time()
    elapsed_time = end_time - start_time


    # returning each iteration details in a row of a 2d list to print it using dataframe
    data = []
    for x in range(len(x0_list)):
        row = []
        row.append(x0_list[x])
        row.append(x1_list[x])
        row.append(tolerance_list[x])
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
    # equation = "exp(-x)-x"
    equation = input("Enter function :\n\n")
    # equation = equation.split("=", 1)[0]
    x0 = float(input("X0 = "))
    # x0 = 0
    epsilon = float(input("Epsilon = "))
    # epsilon = 0.00001
    max_iterations = int(input("Maximum Iterations = "))
    # max_iterations = 50
    Newten_data = newtenraphson(equation,x_i=x0,maxItr=max_iterations,eps=epsilon)
    elapsed_time = Newten_data[len(Newten_data)-1]
    Newten_data.pop(len(Newten_data)-1)
    root = Newten_data[len(Newten_data)-1][1]
    precision = Newten_data[len(Newten_data)-1][2]
    iterations = len(Newten_data)

    print(pd.DataFrame(Newten_data, index=range(1, iterations+1), columns=["X_i", "X_i+1", "Relative Error"]))
    print("\nApproximate root is = %f" % root)
    print("\nElapsed time is %f seconds" % elapsed_time)
    print("\nPrecision is %f\n" % precision)
    print("\n iterations is %f\n"% iterations)
    plot(equation)
