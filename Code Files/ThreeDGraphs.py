from interface import implements
from Interface import GraphInterface
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.ticker as tck
from mpl_toolkits.mplot3d import Axes3D
import math

class ThreeDGraphs(implements(GraphInterface)):
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
