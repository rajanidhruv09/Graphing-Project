from interface import implements
from Interface import GraphInterface
import numpy as np
import matplotlib.pyplot as plt
import math

class TwoDGraphs(implements(GraphInterface)):
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
