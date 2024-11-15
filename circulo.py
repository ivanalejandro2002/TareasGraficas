import pygame
import sys
from pygame import *
import pygame.gfxdraw

pygame.init()
ventana=pygame.display.set_mode((400,300))
pygame.display.set_caption("Tareas")
a=0
b=0
c=0

dr = 255
dg = 255
db = 255

def draw_pixel(x,y):
    pygame.gfxdraw.pixel(ventana,x,y,(dr,dg,db))

def circleSymmetry(xc,yc,x,y):
    draw_pixel(xc + x, yc + y)
    draw_pixel(xc + x, yc - y)
    draw_pixel(xc - x, yc + y)
    draw_pixel(xc - x, yc - y)
    draw_pixel(xc + y, yc + x)
    draw_pixel(xc + y, yc - x)
    draw_pixel(xc - y, yc + x)
    draw_pixel(xc - y, yc - x)

def drawCirle(xc,yc,r):
    x = 0
    y = r
    d = 3 - 2 * r

    circleSymmetry(xc,yc,x,y)

    while(y>=x):

        if(d > 0):
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        
        x += 1

        circleSymmetry(xc,yc,x,y)


def drawEllipseMidPoint(rx,ry,xc,yc):
    x = 0
    y = ry

    d1 = (rx * ry) - (rx*rx*rx) + (0.25+rx*rx)
    dx = 2 * ry * rx * x
    dy = 2 * rx * rx * y

    while(dx < dy):
        draw_pixel(x + xc, yc + y)
        draw_pixel(xc - x, yc + y)
        draw_pixel(xc + x, yc - y)
        draw_pixel(xc - x, yc - y)
    
        if(d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

    d2 = ((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry)
    
    while(y >= 0):
        draw_pixel(xc + x, yc + y)
        draw_pixel(xc - x, yc + y)
        draw_pixel(xc + x, yc - y)
        draw_pixel(xc - x, yc - y)

        if(d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)






def draw_polygon_border(points, color):
    pygame.draw.polygon(ventana, color, points, 1)

def scanline_fill(points, fill_color):
    
    min_y = min(y for _, y in points)
    max_y = max(y for _, y in points)
    
    
    edges = []
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        if p1[1] != p2[1]: 
            if p1[1] > p2[1]:
                p1, p2 = p2, p1
            edges.append((p1, p2))
    
    for y in range(min_y, max_y + 1):
        intersections = []
        for (p1, p2) in edges:
            if p1[1] <= y < p2[1]:
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                x = p1[0] + (y - p1[1]) * dx / dy
                intersections.append(int(x))
        
        intersections.sort()
        for i in range(0, len(intersections), 2):
            if i + 1 < len(intersections):
                pygame.draw.line(ventana, fill_color, (intersections[i], y), (intersections[i + 1], y))


points = [(30, 30), (120, 30), (105, 90), (60, 120), (30, 75)]
while True:
    #a=a+1
    #b=b+2
    #c=c+4
    #a=a%256
    #b=b%256
    #c=c%256
    colorfondo=(a,b,c)
    ventana.fill(colorfondo)
    tiempoA = pygame.time.get_ticks()
    for evento in pygame.event.get():
        
        if evento.type== QUIT:
            pygame.quit()
            sys.exit()
    
    drawCirle(100,100,50)
    drawEllipseMidPoint(100,50,200,200)
    scanline_fill(points,(dr,dg,db))
    #pygame.draw.line(ventana,(120,180,18),(20,30),(20,30),1)
    #pygame.draw.circle(ventana, (255,25,50),(20,30),15,10)
    tiempoB = pygame.time.get_ticks()

    pygame.time.delay(max(0,(1000//60)-(tiempoB-tiempoA)))
    pygame.display.update()