from graphics import *
import numpy as np
import math


PI=3.141592653589

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)



def loadData(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            line_data = [float(k) for k in line.split(",")]
            data.append(line_data[:3])
            data.append(line_data[3:])

    return np.array(data)


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
    print(points_matrix.shape)
    for i  in range(int(points_matrix.shape[0]/2)):
        plots.append(Line(Point(points_matrix.item(i*2+1, 1), points_matrix.item(i*2+1, 0)), Point(points_matrix.item(i*2, 1), points_matrix.item(i*2, 0))))
        plots[-1].draw(win)

    return plots

def update_plots(win, plots, points_matrix):
    newPlots = []
    for i in range(len(plots)):
        plots[i].undraw()
        newPlots.append(Line(Point(points_matrix.item(i*2+1, 1), points_matrix.item(i*2+1, 0)), Point(points_matrix.item(i*2, 1), points_matrix.item(i*2, 0))))
        newPlots[-1].draw(win)
    
    return newPlots




ZOOMFACTOR = 1
imax = 500
jmax = 500
xz=PI/4
xy=PI/4

if __name__ == "__main__":
    dataset = loadData(sys.argv[1])
    win = GraphWin("My engine", jmax, imax)

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

    

