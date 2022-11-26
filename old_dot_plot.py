from graphics import *
import numpy as np
import math


PI=3.141592653589

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)


def getPoints(dataset, xy, xz, ZOOMFACTOR, imax, jmax):

        transMatrix = np.matrix(
                        [[sin(xz)*cos(xy)*ZOOMFACTOR*imax/2, -sin(xy)*ZOOMFACTOR*jmax/2], 
                         [sin(xz)*sin(xy)*ZOOMFACTOR*imax/2, cos(xy)*ZOOMFACTOR*jmax/2],
                         [-cos(xz)*imax/2 * ZOOMFACTOR, 0]]
                    )

        a = np.empty([len(dataset), 1])
        a.fill(imax/2)
        b = np.empty([len(dataset), 1])
        b.fill(jmax/2)

        addMatrix = np.hstack((a, b))

        output = np.add( np.matmul(dataset, transMatrix), addMatrix)

        return output


def init_plots(win, points_matrix):
    plots = []
    for row in points_matrix:
        plots.append(Circle(Point(row.item(0, 1), row.item(0, 0)), 1))
        plots[-1].draw(win)

    plots[0].setFill('red')
    plots[-1].setFill('green')

    return plots



def update_plots(win, plots, points_matrix):
    newPlots = []
    for i in range(len(plots)):
        plots[i].undraw()
        newPlots.append(Circle(Point(points_matrix.item(i, 1), points_matrix.item(i, 0)), 1))
        newPlots[-1].draw(win)

    newPlots[0].setFill('red')
    newPlots[-1].setFill('green')
    
    return newPlots



def loadData(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append([float(k) for k in line.split(",")])

    return np.array(data)

imax = 500
jmax = 500
xz=PI/4
xy=PI/4
ZOOMFACTOR = 1

if __name__ == "__main__":
    dataset = loadData(sys.argv[1])
    win = GraphWin("My engine", jmax, imax)

    xz=PI/4
    xy=PI/4

    points_matrix = getPoints(dataset, xy, xz, ZOOMFACTOR, imax, jmax)
    plots = init_plots(win, points_matrix)

    while(True):
        try:
            key = win.getKey()

            if(key=="d"):
                xy -= PI/12
            if(key == "a"):
                xy += PI/12
            if(key == "w"):
                xz += PI/12
            if(key == "s"):
                xz-= PI/12

            if(key == "q"):
                ZOOMFACTOR /= 3

            if(key == "e"):
                ZOOMFACTOR *= 3

            if(key == "Escape"):
                win.close()

            points_matrix = getPoints(dataset, xy, xz, ZOOMFACTOR, imax, jmax)

            plots = update_plots(win, plots, points_matrix)

        except:
            print("Window Closed")
            break

    

