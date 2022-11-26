import math
import sys

PI=3.141592653589

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)


def func(x, y):
    return sin(x**2 + y**2)

def funcMake(iterations, span):
    output = []

    for i in range(iterations):
        for j in range(iterations):

            x = -(span/2) + (i/iterations * span)
            y = -(span/2) + (j/iterations * span)

            output.append([x, y, func(x, y)])

    return output

if __name__ == "__main__":
    data = funcMake(100, 10)

    with open(sys.argv[1], 'w') as output_file:
        for point in data:
            output_file.write(f"{point[0]},{point[1]},{point[2]}\n")

