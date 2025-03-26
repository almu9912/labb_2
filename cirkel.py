from tkinter import *
from random import randint
import math

bredd = 800
höjd = 600

def normaliserad_till_pixel(n: float) -> int:
    """Konverterar decimal tal till heltal."""
    return int(n * bredd)

#def pixel_till_normaliserad(p: int) -> float:
    """Konverterar heltal till decimaltal."""
    return float(p / bredd)

def cirkel(img, p_mitt: tuple[float, float], r: float, color: str="#008000"):
    x_mitt = normaliserad_till_pixel(p_mitt[0])
    y_mitt = normaliserad_till_pixel(p_mitt[1])
    r_cirkel = normaliserad_till_pixel(r)

    for y in range(y_mitt - r_cirkel, y_mitt + r_cirkel +1):
        for x in range(x_mitt - r_cirkel, x_mitt + r_cirkel + 1):
            avstånd = math.sqrt((x - x_mitt) ** 2 + (y - y_mitt) ** 2)
            #if (x - normaliserad_till_pixel(p_mitt[0]))**2 + (y - normaliserad_till_pixel(p_mitt[1]))**2 <= (normaliserad_till_pixel(r))**2:
            #epsilon = 0.0001
            if avstånd <= r_cirkel:
                img.put(color, (x, y))
"""Cirkel med radie r och mittpunkt x_y_mitt."""
        

def main():
    fönster = Tk()
    canvas = Canvas(fönster, width=bredd, height=höjd, bg="#000080")
    canvas.pack()
    img = PhotoImage(width=bredd, height=höjd)
    canvas.create_image(0, 0, anchor=NW, image = img)
    cirkel(img, (0.8, 0.2), 0.09, "#FFFF00")
    mainloop()

if __name__ == '__main__':
    main()
