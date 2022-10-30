from pathlib import Path
from tkinter import *
from turtle import delay, window_height
import tkinter
from time import time, sleep




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("390x844")
window.configure(bg = "#7CDAF9")
window.title("CALCULADORA SP")


canvas = Canvas(
    window,
    bg = "#7CDAF9",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: formula1(" NEW WHEELS"),
    relief="flat"
)
button_1.place(
    x=33.0,
    y=334.0,
    width=61.0,
    height=31.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: formula1("BOX, BOX!"),
    relief="flat"
)
button_2.place(
    x=115.0,
    y=334.0,
    width=68.0,
    height=32.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:formula1 ("    ACTIVATED"),
    relief="flat"
)
button_3.place(
    x=202.0,
    y=334.0,
    width=60.0,
    height=32.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: formula1(" CHECO PÉREZ"),
    relief="flat"
)
button_4.place(
    x=286.0,
    y=335.0,
    width=60.0,
    height=30.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: borrarac(),
    relief="flat"
)
button_5.place(
    x=34.0,
    y=376.0,
    width=60.0,
    height=60.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command = lambda: click("("),
    relief="flat"
)
button_6.place(
    x=117.0,
    y=377.0,
    width=63.0,
    height=59.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(")"),
    relief="flat"
)
button_7.place(
    x=201.0,
    y=376.0,
    width=61.0,
    height=60.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("*"),
    relief="flat"
)
button_8.place(
    x=285.0,
    y=453.0,
    width=61.0,
    height=60.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("/"),
    relief="flat"
)
button_9.place(
    x=285.0,
    y=377.0,
    width=61.0,
    height=59.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    194.5,
    163.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#2196F3",
    highlightthickness=0,
    font= ("Chakra Petch SemiBold",  30),
    foreground="white"
    
)
entry_1.place(
    x=46.0,
    y=24.0,
    width=297.0,
    height=277.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(7),
    relief="flat"
)
button_10.place(
    x=33.0,
    y=451.0,
    width=61.0,
    height=62.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(8),
    relief="flat"
)
button_11.place(
    x=117.0,
    y=451.0,
    width=63.0,
    height=62.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(9),
    relief="flat"
)
button_12.place(
    x=195.0,
    y=452.0,
    width=71.0,
    height=61.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(4),
    relief="flat"
)
button_13.place(
    x=30.0,
    y=530.0,
    width=67.0,
    height=60.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(5),
    relief="flat"
)
button_14.place(
    x=116.0,
    y=527.0,
    width=64.0,
    height=63.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(6),
    relief="flat"
)
button_15.place(
    x=195.0,
    y=528.0,
    width=71.0,
    height=62.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("+"),
    relief="flat"
)
button_16.place(
    x=281.0,
    y=526.0,
    width=69.0,
    height=64.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(1),
    relief="flat"
)
button_17.place(
    x=33.0,
    y=604.0,
    width=64.0,
    height=63.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(2),
    relief="flat"
)
button_18.place(
    x=114.0,
    y=606.0,
    width=69.0,
    height=65.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(3),
    relief="flat"
)
button_19.place(
    x=195.0, 
    y=605.0,
    width=71.0,
    height=62.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("-"),
    relief="flat"
)
button_20.place(
    x=284.0,
    y=606.0,
    width=66.0,
    height=65.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(0),
    relief="flat"
)
button_21.place(
    x=30.0,
    y=682.0,
    width=67.0,
    height=65.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("00"),
    relief="flat"
)
button_22.place(
    x=117.0,
    y=682.0,
    width=63.0,
    height=65.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("."),
    relief="flat"
)
button_23.place(
    x=195.0,
    y=684.0,
    width=71.0,
    height=63.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: igual(),
    relief="flat"
)
button_24.place(
    x=281.0,
    y=681.0,
    width=73.0,
    height=66.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("+"),
    relief="flat"
)
button_25.place(
    x=28.0,
    y=759.0,
    width=72.0,
    height=32.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_26 clicked"),
    relief="flat"
)
button_26.place(
    x=137.0,
    y=758.0,
    width=112.0,
    height=39.0
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("-"),
    relief="flat"
)
button_27.place(
    x=285.0,
    y=759.0,
    width=69.0,
    height=38.0
)

button_image_28 = PhotoImage(
    file=relative_to_assets("button_28.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: formula1("RED BULL 2022"),
    relief="flat"
)
button_28.place(
    x=35.0,
    y=804.0,
    width=304.0,
    height=32.0
)


i = 0

def click(valor):
    global i
    entry_1.insert(i, valor)
    i += 1

def borrarac():
    entry_1.delete(0, END)
    i = 0   

def igual():
    ecuacion = entry_1.get()
    resulato = eval(ecuacion)
    entry_1.delete(0, END)
    entry_1.insert(0, resulato)
    i = 0    

def formula1(valor):
    global i
    entry_1.insert(i, valor)
    i += 1
    entry_1.after(1000, borrarac)
   
    


    
       
    


    


        

    
    
    
    

window.resizable(False, False)
window.mainloop()
