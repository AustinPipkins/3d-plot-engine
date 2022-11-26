import math
import sys


CNOTE=261.63
ENOTE=329.63
GNOTE=392

def sin(x):
    return math.sin(x)

def getVal(freq, time):
    return sin(time/freq)


def cMajor(iterations, step):
    time = 0

    output = []

    for i in range(iterations):
        time += step

        output.append([getVal(CNOTE, time), getVal(ENOTE, time), getVal(GNOTE, time), getVal(CNOTE, time+step), getVal(ENOTE, time+step), getVal(GNOTE, time+step)])

    return output

if __name__ == "__main__":
    data = cMajor(1000, 50)

    with open(sys.argv[1], 'w+') as output_file:
        for point in data:
            output_file.write(f"{point[0]},{point[1]},{point[2]},{point[3]},{point[4]},{point[5]}\n")