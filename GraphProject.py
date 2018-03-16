from TwoDGraphs import TwoDGraphs
from ThreeDGraphs import ThreeDGraphs

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
   

