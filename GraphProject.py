import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from mpl_toolkits.mplot3d import Axes3D
import math


class TwoDGraphs:
        def __init__(self):
                self
        def line(self):
                m = float(input("Enter the value of m: "))
                b = float(input("Enter the value of b: "))
                start = float(input("Enter the starting value of x: "))
                end = float(input("Enter the end value of x: "))
                xValues = np.arange(start, end + 1)
                yValues = m * xValues + b
                plt.plot(xValues, yValues)
                plt.xlabel("x-Axis")
                plt.ylabel("y-Axis")
                plt.title("Graph of y = " + str(m) + "x + " +  str(b) )
                plt.grid()
                plt.show()
        def quadratic(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                start = float(input("Enter the starting value of x: "))
                end = float(input("Enter the end value of x: "))
                xValues = np.arange(start, (end + 1), 0.001)
                yValues = a*(xValues ** 2) + b * xValues + c
                plt.plot(xValues, yValues)
                plt.xlabel("x-Axis")
                plt.ylabel("y-Axis")
                plt.title("Graph of y = " + str(a) + "x^2 + " +  str(b) + "x + " + str(c) )
                plt.grid()
                plt.show()
        def cubic(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                start = float(input("Enter the starting value of x: "))
                end = float(input("Enter the end value of x: "))
                xValues = np.arange(start, (end + 1), 0.001)
                yValues = a*(xValues ** 3) + b * (xValues**2) + c * xValues + d
                plt.plot(xValues, yValues)
                plt.xlabel("x-Axis")
                plt.ylabel("y-Axis")
                plt.title("Graph of y = " + str(a) + "x^3 + " +  str(b) + "x^2 + " + str(c) + "x + " + str(d) )
                plt.grid()
                plt.show()
        def quartic(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                e = float(input("Enter the value of e: "))
                start = float(input("Enter the starting value of x: "))
                end = float(input("Enter the end value of x: "))
                xValues = np.arange(start, (end + 1), 0.001)
                yValues = a*(xValues ** 4) + b * (xValues**3) + c * (xValues**2) + d * xValues + e
                plt.plot(xValues, yValues)
                plt.xlabel("x-Axis")
                plt.ylabel("y-Axis")
                plt.title("Graph of y = " + str(a) + "x^4 + " +  str(b) + "x^3 + " + str(c) + "x^2 + " + str(d) + "x + " + str(e) )
                plt.grid()
                plt.show()
        def sin(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.arange(-2*math.pi, 2*math.pi, 0.001)
                yValues = a * np.sin(b * xValues + c) + d
                plt.plot(xValues, yValues)
                plt.xticks(np.linspace(-2*np.pi, 2*np.pi, 9),\
                ['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'], fontsize= 10)
                plt.xlabel("x-Axis")
                plt.ylabel("y-Axis")
                plt.title("Graph of y = " + str(a) + "sin( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.grid()
                plt.show()
        def cos(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.arange(-2*math.pi, 2*math.pi, 0.001)
                yValues = a * np.cos(b * xValues + c) + d
                plt.plot(xValues, yValues)
                plt.xticks(np.linspace(-2*np.pi, 2*np.pi, 9),\
                ['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'], fontsize= 10)
                plt.xlabel("x-Axis")
                plt.ylabel("y-Axis")
                plt.title("Graph of y = " + str(a) + "cos( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.grid()
                plt.show()
        def tan(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.linspace(-2*math.pi, 2*math.pi, 10000)
                yValues = a * np.tan(b * xValues + c) + d

                tol = 20
                negTol = -20
                yValues[yValues > tol] = np.inf
                yValues[yValues < negTol] = -np.inf
                
                plt.plot(xValues, yValues)
                plt.xticks(np.linspace(-2*np.pi, 2*np.pi, 9),\
                ['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'], fontsize= 10)
                plt.xlabel("x-Axis")
                plt.ylabel("y-Axis")
                plt.title("Graph of y = " + str(a) + "tan( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.grid()
                plt.show()
        def sec(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.linspace(-2*math.pi, 2*math.pi, 10000)
                yValues = 1 / (a * np.cos(b * xValues + c) + d)

                tol = 20
                negTol = -20
                yValues[yValues > tol] = np.inf
                yValues[yValues < negTol] = -np.inf
                
                plt.plot(xValues, yValues)
                plt.xticks(np.linspace(-2*np.pi, 2*np.pi, 9),\
                ['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'], fontsize= 10)
                plt.xlabel("x-Axis")
                plt.ylabel("y-Axis")
                plt.title("Graph of y = " + str(a) + "sec( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.grid()
                plt.show()
        def csc(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.linspace(-2*math.pi, 2*math.pi, 10000)
                yValues = 1 / (a * np.sin(b * xValues + c) + d)

                tol = 20
                negTol = -20
                yValues[yValues > tol] = np.inf
                yValues[yValues < negTol] = -np.inf
                
                plt.plot(xValues, yValues)
                plt.xticks(np.linspace(-2*np.pi, 2*np.pi, 9),\
                ['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'], fontsize= 10)
                plt.xlabel("x-Axis")
                plt.ylabel("y-Axis")
                plt.title("Graph of y = " + str(a) + "csc( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.grid()
                plt.show()
        def cot(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.linspace(-2*math.pi, 2*math.pi, 10000)
                yValues = 1 / (a*(np.tan(b * xValues + c) + d))

                tol = 20
                negTol = -20
                yValues[yValues > tol] = np.inf
                yValues[yValues < negTol] = -np.inf

                plt.plot(xValues, yValues)
                plt.xticks(np.linspace(-2*np.pi, 2*np.pi, 9), \
                ['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'], fontsize= 10)
                plt.xlabel("x-Axis")
                plt.ylabel("y-Axis")
                plt.title("Graph of y = " + str(a) + "cot( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.grid()
                plt.show()
        
                
class ThreeDGraphs:
        def __init__(self):
                self
        def line(self):
                m = float(input("Enter the value of m: "))
                b = float(input("Enter the value of b: "))
                start = float(input("Enter the starting value of x: "))
                end = float(input("Enter the end value of x: "))
                xValues = np.arange(start, (end + 1))
                yValues = m * xValues + b
                fig = plt.figure()
                ax = fig.add_subplot(111, projection = '3d')
                ax.set_zlim(0,1)
                ax.view_init(elev=57., azim=-77)
                ax.plot(xValues, yValues)
                ax.set_xlabel("x-Axis")
                ax.set_ylabel("y-Axis")
                ax.set_zlabel("z-Axis")
                ax.set_title("Graph of y = " + str(m) + "x + " +  str(b) )
                plt.show()
        def quadratic(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                start = float(input("Enter the starting value of x: "))
                end = float(input("Enter the end value of x: "))
                xValues = np.arange(start, (end + 1), 0.001)
                yValues = a*(xValues ** 2) + b * xValues + c
                fig = plt.figure()
                ax = fig.add_subplot(111, projection = '3d')
                ax.set_zlim(0,1)
                ax.view_init(elev=57., azim=-77)
                ax.plot(xValues, yValues)
                ax.set_xlabel("x-Axis")
                ax.set_ylabel("y-Axis")
                ax.set_zlabel("z-Axis")
                ax.set_title("Graph of y = " + str(a) + "x^2 + " +  str(b) + "x + " + str(c) )
                plt.show()
        def cubic(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                start = float(input("Enter the starting value of x: "))
                end = float(input("Enter the end value of x: "))
                xValues = np.arange(start, (end + 1), 0.001)
                yValues = a*(xValues ** 3) + b * (xValues**2) + c*xValues + d
                fig = plt.figure()
                ax = fig.add_subplot(111, projection = '3d')
                ax.set_zlim(0,1)
                ax.view_init(elev = 57., azim = -77)
                ax.plot(xValues, yValues)
                ax.set_xlabel("x-Axis")
                ax.set_ylabel("y-Axis")
                ax.set_zlabel("z-Axis")
                ax.set_title("Graph of y = " + str(a) + "x^3 + " +  str(b) + "x^2 + " + str(c) + "x + " + str(d) )
                plt.show()
        def quartic(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                e = float(input("Enter the value of e: "))
                start = float(input("Enter the starting value of x: "))
                end = float(input("Enter the end value of x: "))
                xValues = np.arange(start, (end + 1), 0.001)
                yValues = (a*(xValues ** 4)) + (b * (xValues**3)) + (c * (xValues**2)) + (d * xValues) + e
                fig = plt.figure()
                ax = fig.add_subplot(111, projection = '3d')
                ax.set_zlim(0,1)
                ax.view_init(elev = 57., azim = -77)
                ax.plot(xValues, yValues)
                ax.set_xlabel("x-Axis")
                ax.set_ylabel("y-Axis")
                ax.set_zlabel("z-Axis")
                ax.set_title("Graph of y = " + str(a) + "x^4 + " +  str(b) + "x^3 + " + str(c) + "x^2 + " + str(d) + "x + " + str(e) )
                plt.show()
        def sin(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.arange(-2*math.pi, 2*math.pi, 0.001)
                yValues = a * np.sin(b * xValues + c) + d
                fig = plt.figure()
                ax = fig.add_subplot(111, projection = '3d')
                ax.set_zlim(0,1)
                ax.view_init(elev = 57., azim = -77)
                ax.plot(xValues, yValues)
                ax.set_xticklabels(['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'])
                ax.set_xlabel("x-Axis")
                ax.set_ylabel("y-Axis")
                ax.set_zlabel("z-Axis")
                ax.set_title("Graph of y = " + str(a) + "sin( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.show()
        def cos(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.arange(-2*math.pi, 2*math.pi, 0.001)
                yValues = a * np.cos(b * xValues + c) + d
                fig = plt.figure()
                ax = fig.add_subplot(111, projection = '3d')
                ax.set_zlim(0,1)
                ax.view_init(elev = 57., azim = -77)
                ax.plot(xValues, yValues)
                ax.set_xticklabels(['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'])
                ax.set_xlabel("x-Axis")
                ax.set_ylabel("y-Axis")
                ax.set_zlabel("z-Axis")
                ax.set_title("Graph of y = " + str(a) + "cos( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.show()
        def tan(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.arange(-2*math.pi, 2*math.pi, 0.001)
                yValues = a * np.tan(b * xValues + c) + d

                tol = 20
                negTol = -20
                yValues[yValues > tol] = np.inf
                yValues[yValues < negTol] = -np.inf
                
                fig = plt.figure()
                ax = fig.add_subplot(111, projection = '3d')
                ax.set_zlim(0,1)
                ax.view_init(elev = 57., azim = -77)
                ax.plot(xValues, yValues)
                ax.set_xticklabels(['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'])
                ax.set_xlabel("x-Axis")
                ax.set_ylabel("y-Axis")
                ax.set_zlabel("z-Axis")
                ax.set_title("Graph of y = " + str(a) + "tan( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.show()
        def sec(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.arange(-2*math.pi, 2*math.pi, 0.001)
                yValues = 1/ (a * np.cos(b * xValues + c) + d)
                
                tol = 20
                negTol = -20
                yValues[yValues > tol] = np.inf
                yValues[yValues < negTol] = -np.inf
                
                fig = plt.figure()
                ax = fig.add_subplot(111, projection = '3d')
                ax.set_zlim(0,1)
                ax.view_init(elev = 57., azim = -77)
                ax.plot(xValues, yValues)
                ax.set_xticklabels(['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'])
                ax.set_xlabel("x-Axis")
                ax.set_ylabel("y-Axis")
                ax.set_zlabel("z-Axis")
                ax.set_title("Graph of y = " + str(a) + "sec( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.show()
        def csc(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.arange(-2*math.pi, 2*math.pi, 0.001)
                yValues = 1 / (a * np.sin(b * xValues + c) + d)

                tol = 20
                negTol = -20
                yValues[yValues > tol] = np.inf
                yValues[yValues < negTol] = -np.inf

                fig = plt.figure()
                ax = fig.add_subplot(111, projection = '3d')
                ax.set_zlim(0,1)
                ax.view_init(elev = 57., azim = -77)
                ax.plot(xValues, yValues)
                ax.set_xticklabels(['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'])
                ax.set_xlabel("x-Axis")
                ax.set_ylabel("y-Axis")
                ax.set_zlabel("z-Axis")
                ax.set_title("Graph of y = " + str(a) + "csc( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.show()
        def cot(self):
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c: "))
                d = float(input("Enter the value of d: "))
                print("The graph of this trigonometric function is going to be from -2pi to 2pi")
                xValues = np.arange(-2*math.pi, 2*math.pi, 0.001)
                yValues = 1 / (a * np.tan(b * xValues + c) + d)

                tol = 20
                negTol = -20
                yValues[yValues > tol] = np.inf
                yValues[yValues < negTol] = -np.inf
                
                fig = plt.figure()
                ax = fig.add_subplot(111, projection = '3d')
                ax.set_zlim(0,1)
                ax.view_init(elev = 57., azim = -77)
                ax.plot(xValues, yValues)

                ax.set_xticklabels(['$-2\pi$', '$-3\pi/2$','$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'])
                ax.set_xlabel("x-Axis")
                ax.set_ylabel("y-Axis")
                ax.set_zlabel("z-Axis")
                ax.set_title("Graph of y = " + str(a) + "cot( " + str(b) + "x + " + str(c) + ") " + str(d))
                plt.show()

graphs2d = TwoDGraphs()
graphs3d = ThreeDGraphs()
print("Please choose the type of graph you want to create")
print("1. 2-Dimentional Graph")
print("2. 3-Dimentional Graph")
choice1 = int(input("Your choice: "))

if choice1 == 1:
        print("Choose the type of graphs from the following menu")
        print("1. Graphs of polynomials")
        print("2. Graphs of trigonometric functions")
        print("3. Graphs of logarithmic functions")
        print("4. Graphs of statistical functions")
        choice2 = int(input("Your Choice: "))
        if choice2 == 1:
                print("1. y = mx + b")
                print("2. y = ax^2 + bx + c")
                print("3. y = ax^3 + bx^2 + cx + d")
                print("4. y = ax^4 + bx^3 + c^2 + dx + e")
                choice3 = int(input("Your choice: "))
                if choice3 == 1:
                        graphs2d.line()
                elif choice3 == 2:
                        graphs2d.quadratic()
                elif choice3 == 3:
                        graphs2d.cubic()
                elif choice3 == 4:
                        graphs2d.quartic()
                else:
                        print("Wrong choice input")
        elif choice2 == 2:
                print("1. a*sin(bx + c) + d")
                print("2. a*cos(bx + c) + d")
                print("3. a*tan(bx + c) + d")
                print("4. a*sec(bx + c) + d")
                print("5. a*csc(bx + c) + d")
                print("6. a*cot(bx + c) + d")
                choice3 = int(input("Your choice: "))
                if choice3 == 1:
                        graphs2d.sin()
                elif choice3 == 2:
                        graphs2d.cos()
                elif choice3 == 3:
                        graphs2d.tan()
                elif choice3 == 4:
                        graphs2d.sec()
                elif choice3 == 5:
                        graphs2d.csc()
                elif choice3 == 6:
                        graphs2d.cot()
                else:
                        print("Wrong choice input")
                
elif choice1 == 2:
        print("Choose the type of graphs from the following menu")
        print("1. Graphs of polynomials")
        print("2. Graphs of trigonometric functions")
        print("3. Graphs of logarithmic functions")
        print("4. Graphs of statistical functions")
        choice2 = int(input("Your Choice: "))
        if choice2 == 1:
                print("1. y = mx + b")
                print("2. y = ax^2 + bx + c")
                print("3. y = ax^3 + bx^2 + cx + d")
                print("4. y = ax^4 + bx^3 + c^2 + dx + e")
                choice3 = int(input("Your choice: "))
                if choice3 == 1:
                        graphs3d.line()
                elif choice3 == 2:
                        graphs3d.quadratic()
                elif choice3 == 3:
                        graphs3d.cubic()
                elif choice3 == 4:
                        graphs3d.quartic()
                else:
                        print("Wrong choice input")
        elif choice2 == 2:
                print("1. a*sin(bx + c) + d")
                print("2. a*cos(bx + c) + d")
                print("3. a*tan(bx + c) + d")
                print("4. a*sec(bx + c) + d")
                print("5. a*csc(bx + c) + d")
                print("6. a*cot(bx + c) + d")
                choice3 = int(input("Your choice: "))
                if choice3 == 1:
                        graphs3d.sin()
                elif choice3 == 2:
                        graphs3d.cos()
                elif choice3 == 3:
                        graphs3d.tan()
                elif choice3 == 4:
                        graphs3d.sec()
                elif choice3 == 5:
                        graphs3d.csc()
                elif choice3 == 6:
                        graphs3d.cot()
                else:
                        print("Wrong choice input")
   

