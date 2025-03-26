import tkinter as tk
from random import randint
import math

width = 800
height = 600

def normaliserad_till_pixel_x(n: float) -> int:
    return int(n * width)

def normaliserad_till_pixel_y(n: float) -> int:
    return int(n * height)

def triangel(img, p1, p2, p3, color="#008080"):
    """Ritar en triangel med tre hörn i normaliserade koordinater."""

    # Konvertera normaliserade koordinater till pixlar
    p1 = (normaliserad_till_pixel_x(p1[0]), normaliserad_till_pixel_y(p1[1]))
    p2 = (normaliserad_till_pixel_x(p2[0]), normaliserad_till_pixel_y(p2[1]))
    p3 = (normaliserad_till_pixel_x(p3[0]), normaliserad_till_pixel_y(p3[1]))

    def area(p1, p2, p3):
        """Beräknar triangelns area med Herons formel."""
        a = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        b = math.sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
        c = math.sqrt((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    x_min = min(p1[0], p2[0], p3[0])
    x_max = max(p1[0], p2[0], p3[0])
    y_min = min(p1[1], p2[1], p3[1])
    y_max = max(p1[1], p2[1], p3[1])

    epsilon = 0.0001
    A_tot = area(p1, p2, p3)

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            punkt = (x, y)
            A1 = area(punkt, p1, p2)
            A2 = area(p3, punkt, p2)
            A3 = area(p3, p1, punkt)
            if abs(A_tot - (A1 + A2 + A3)) <= epsilon:
                if randint(0, 1) == 0:
                    img.put(color, (x, y))

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=width, height=height, bg="#800000")
    canvas.pack()

    img = tk.PhotoImage(width=width, height=height)
    canvas.create_image((0, 0), image=img, anchor=tk.NW)

    triangel(img, (0.5, 0.1), (0.1, 0.6), (0.9, 0.6), color="#00FFFF")

    root.mainloop()

if __name__ == '__main__':
    main()
