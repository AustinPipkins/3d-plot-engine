from ast import expr_context
import pygame
from pygame.locals import *
import sys
import math
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

PI=3.141592653589

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

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


def plot_lines(screen, points_matrix):
    screen.fill(BLACK)


    for i in range(int(points_matrix.shape[0]/2)):
        pygame.draw.line(screen, GREEN, [points_matrix.item(i*2+1, 1), points_matrix.item(i*2+1, 0)], [points_matrix.item(i*2, 1), points_matrix.item(i*2, 0)], 1)

    pygame.display.update()


def loadData(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            line_data = [float(k) for k in line.split(",")]
            data.append(line_data[:3])
            data.append(line_data[3:])

    return np.array(data)

ZOOMFACTOR = 1
imax = 500
jmax = 500
SCREEN_SIZE = WIDTH, HEIGHT = (imax, jmax)
xz=PI/4
xy=PI/4

if __name__ == "__main__":
    dataset = loadData(sys.argv[1])


    # Initialization
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('My Engine')


    points_matrix = getPoints(dataset, xy, xz, ZOOMFACTOR, imax, jmax)
    plot_lines(screen, points_matrix)
    fps = pygame.time.Clock()


    moveDenom = 24
    zoomDenom = 1.3

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEWHEEL:
                    ZOOMFACTOR *= zoomDenom ** event.y

            keys = pygame.key.get_pressed()  #checking pressed keys
            if keys[pygame.K_a]:
                xy -= PI/moveDenom

            if keys[pygame.K_d]:
                xy += PI/moveDenom

            if keys[pygame.K_s]:
                xz += PI/moveDenom

            if keys[pygame.K_w]:
                xz-= PI/moveDenom

            if keys[pygame.K_q]:
                ZOOMFACTOR /= zoomDenom

            if keys[pygame.K_e]:
                ZOOMFACTOR *= zoomDenom

            points_matrix = getPoints(dataset, xy, xz, ZOOMFACTOR, imax, jmax)

            plot_lines(screen, points_matrix)

            fps.tick(10)

        except:
            print("Window Closed")
            break
