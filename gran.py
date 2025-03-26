from tkinter import *
from random import randint
import math

bredd = 800
höjd = 600

def normaliserad_till_pixel_x(n: float) -> int:
    return int(n * bredd)

def normaliserad_till_pixel_y(n: float) -> int:
    return int(n * höjd)

def pixel_till_normaliserad(p: int) -> float:
    return float(p / bredd)

def stam(img, p1: tuple[float, float], p2: tuple[float, float], color: str="#FFFF00"):
    for y in range(normaliserad_till_pixel_y(p1[1]), normaliserad_till_pixel_y(p2[1])):
        for x in range(normaliserad_till_pixel_x(p1[0]), normaliserad_till_pixel_x(p2[0])):
            img.put(color, (x,y))

def gren(img, q1, q2, q3, color: str="#800000"):
    q1 = (normaliserad_till_pixel_x(q1[0]), normaliserad_till_pixel_y(q1[1]))
    q2 = (normaliserad_till_pixel_x(q2[0]), normaliserad_till_pixel_y(q2[1]))
    q3 = (normaliserad_till_pixel_x(q3[0]), normaliserad_till_pixel_y(q3[1]))

    def area(q1, q2, q3):
        a = math.sqrt((q1[0] - q2[0]) ** 2 + (q1[1] - q2[1]) ** 2)
        b = math.sqrt((q2[0] - q3[0]) ** 2 + (q2[1] - q3[1]) ** 2)
        c = math.sqrt((q3[0] - q1[0]) ** 2 + (q3[1] - q1[1]) ** 2)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    x_min = min(q1[0], q2[0], q3[0])
    x_max = max(q1[0], q2[0], q3[0])
    y_min = min(q1[1], q2[1], q3[1])
    y_max = max(q1[1], q2[1], q3[1])

    epsilon = 0.0001
    A_tot = area(q1, q2, q3)

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            punkt = (x, y)
            A1 = area(punkt, q1, q2) 
            A2 = area( q3, punkt, q2)
            A3 = area(q3, q1, punkt)
            if abs(A_tot - (A1 + A2 + A3)) <= epsilon:
                img.put(color, (x, y))


def main():
    fönster = Tk()
    canvas = Canvas(fönster, width=bredd, height=höjd, bg="#800080")
    canvas.pack()
    img = PhotoImage(width=bredd, height=höjd)
    canvas.create_image((bredd // 2, höjd // 2), image=img, state="normal")
    stam(img, (0.2, 0.7), (0.3, 0.99), color="#8B4513")
    gren(img, (0.25, 0.45), (0.1, 0.7), (0.4, 0.7), color="#008000")
    i = 0
    y_uppåt = 0
    while i < 3:
        gren(img, (0.25, 0.45 - y_uppåt), (0.1, 0.7 - y_uppåt), (0.4, 0.7 - y_uppåt), color="#008000")
        y_uppåt += 0.1
        i += 1
    mainloop()

if __name__=='__main__':
    main()
