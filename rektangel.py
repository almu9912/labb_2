from tkinter import *

BREDD = 800
HÖJD = 600

def normaliserad_till_pixel(n: float) -> int:
    """Konverterar normaliseradvärde till pixelvärde."""
    return int(n *  BREDD)

def pixel_till_normaliserad(p: int) -> float:
    """Konverterar pixelvärde till normaliseradvärde."""
    return p / BREDD

def rektangel(img, övre_vänster: tuple[float, float], nedre_höger: tuple[float, float], color: str="#ffffff"):
    for y in range(normaliserad_till_pixel(övre_vänster[1]), normaliserad_till_pixel(nedre_höger[1])):
        for x in range(normaliserad_till_pixel(övre_vänster[0]), normaliserad_till_pixel(nedre_höger[0])):
            img.put(color, (x, y))

def main():
    fönster = Tk()
    canvas = Canvas(fönster, width=BREDD, height=HÖJD, bg="#000080")
    canvas.pack()
    img = PhotoImage(width=BREDD, height=HÖJD)
    canvas.create_image((BREDD / 2, HÖJD/ 2), image=img, state="normal")
    rektangel(img, (0.3, 0.185), (0.7, 0.585), "#FFFF00")
    mainloop()

if __name__ == '__main__':
    main()

