from tkinter import *
from random import randint

width = 800
height = 600

def normaliserad_till_pixel(n: float) -> int:
    """Konverterar decimal tal till heltal"""
    return int(n * height)

def pixel_till_normaliserad(p: int) -> float:
    """Konverterar heltal till decimaltal."""
    return float(p / width)

def triangel(img, rätvinklig_hörn: tuple[float, float], liggande_katet: float, stående_katet: float, color: str="#008080"):
    x0 = normaliserad_till_pixel(rätvinklig_hörn[0])
    y0 = normaliserad_till_pixel(rätvinklig_hörn[1])
    längd = normaliserad_till_pixel(liggande_katet)
    höjd = normaliserad_till_pixel(stående_katet)
    for y in range(y0, y0 + höjd):
        x_max = x0 + (längd * (y - y0)) // höjd
        for x in range(x0, x0 + längd):
            if x <= x_max:
                if randint(0, 1) == 0:
                    img.put(color, (x, y))

def main():
    fönster = Tk()
    canvas = Canvas(fönster, width=width, height=height, bg = "#800000")
    canvas.pack()
    img = PhotoImage(width=width, height=height)
    canvas.create_image(width // 2, height // 2, image=img, state="normal")
    triangel(img, (0.7, 0.4), 0.3, 0.4, color="#00FFFF")
    """Jag kan inte använda negativa koordinater, hur kan jag ha en triangel som löser alla fyra möjliga fall???"""
    mainloop()

if __name__ == '__main__':
    main()

    
