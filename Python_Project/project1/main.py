"""
Bluiding the super minesweeper game
BY: James Toma Alpha
file: main.py
"""
from tkinter import *
import settings
import utils
from cell import Cell

#create the game window for the mine sweeper 
root = Tk()
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False, False)
root.title("Mine Sweeper")

# create the game frame
# the top frame
top_frame = Frame(
    root,
    width=settings.WIDTH,
    height=utils.percentage_height(25),
    bg="purple"
)
top_frame.place(x=0, y=0)

# game title
title = Label(
    top_frame,
    width=20,
    height=2,
    text="Mine Swipper Game",
    font=("", 30)
)
title.place(x=500, y=0)

# the left frame
left_frame = Frame(
    root, 
    width=utils.percentage_width(25),
    height=utils.percentage_height(75),
    bg="bisque4"
)
left_frame.place(x=0, y=utils.percentage_height(25))

# the right frame
center_frame = Frame(
    root,
    width=utils.percentage_width(75),
    height=utils.percentage_height(75),
    bg="BlanchedAlmond"
)
center_frame.place(x=utils.percentage_width(25), y=utils.percentage_height(25))


# put the bottons on the center frame 
for i in range(settings.GRID_SIZE):
    for j in range(settings.GRID_SIZE):
        c = Cell(i, j)
        c.create_button_obj(center_frame)
        c.btn_obj.grid(column=j, row=i)

Cell.randomise_cell()

# place the label on the left side of the screen
Cell.create_label_obj(left_frame)
Cell.label_obj.place(x=0, y=0)





root.mainloop()