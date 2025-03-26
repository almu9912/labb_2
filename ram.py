from tkinter import *
from random import randint

BREDD = 800
HÖJD = 600

def normaliserad_till_pixel(n: float) -> int:
    """Konverterar normaliseradvärde till pixelvärde."""
    return int(n *  BREDD)

def pixel_till_normaliserad(p: int) -> float:
    """Konverterar pixelvärde till normaliseradvärde."""
    return p / BREDD

def random_ram_vänster(img, övre_vänster: tuple[float, float], nedre_vänster: tuple[float, float], color: str="#800080"):
    for y in range(normaliserad_till_pixel(övre_vänster[1]), normaliserad_till_pixel(nedre_vänster[1])):
        for x in range(normaliserad_till_pixel(övre_vänster[0]), normaliserad_till_pixel(nedre_vänster[0])):
            if randint(0, 1) == 0:
                img.put(color, (x, y))

def random_ram_höger(img, övre_höger: tuple[float, float], nedre_höger: tuple[float, float], color: str="#800080"):  
    for y in range(normaliserad_till_pixel(övre_höger[1]), normaliserad_till_pixel(nedre_höger[1])):
        for x in range(normaliserad_till_pixel(övre_höger[0]), normaliserad_till_pixel(nedre_höger[0])):
             if randint(0, 1) == 0:
                img.put(color, (x, y))
                                
def random_ram_övre(img, övre_övre: tuple[float, float], övre_nedre: tuple[float, float], color: str="#800080"):
     for y in range(normaliserad_till_pixel(övre_övre[1]), normaliserad_till_pixel(övre_nedre[1])):
           for x in range(normaliserad_till_pixel(övre_övre[0]), normaliserad_till_pixel(övre_nedre[0])):
            if randint(0, 1) == 0:
                  img.put(color, (x, y))
                 
def random_ram_nedre(img, nedre_övre: tuple[float, float], nedre_nedre: tuple[float, float], color: str="#800080"):
     for y in range(normaliserad_till_pixel(nedre_övre[1]), normaliserad_till_pixel(nedre_nedre[1])):
        for x in range(normaliserad_till_pixel(nedre_övre[0]), normaliserad_till_pixel(nedre_nedre[0])):
             if randint(0, 1) == 0:
                   img.put(color, (x, y))              

def main():
    ram = Tk()
    canvas = Canvas(ram, width=BREDD, height=HÖJD, bg="#000080")
    canvas.pack()
    img = PhotoImage(width=BREDD, height=HÖJD)
    canvas.create_image((BREDD / 2, HÖJD/ 2), image=img, state="normal")
    random_ram_vänster(img, (0.01, 0.01), (0.02, 0.74))
    random_ram_höger(img, (0.98, 0.01), (0.99, 0.74))
    random_ram_övre(img, (0.02, 0.01), (0.98, 0.02))
    random_ram_nedre(img, (0.02, 0.73), (0.98, 0.74))
    mainloop()

if __name__ == '__main__':
    main()

