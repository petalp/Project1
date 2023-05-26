from tkinter import Button, Label
import random
import settings
import sys



class Cell:
    all = []
    label_obj = None
    cell_count = settings.CELL_COUNTS

    def __init__(self,x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.cell_mine = True
        self.btn_obj = None
        self.x = x
        self.y = y

        # add each object to the class attribute
        Cell.all.append(self)


    def create_button_obj(self, location):
        """Create a button for each cell object"""
        btn = Button(
            location, 
            width=15,
            height=3,
            bg="chocolate3"
            )
        btn.bind("<Button-1>", self.left_clicked)
        btn.bind("<Button-3>", self.right_clicked)

        self.btn_obj = btn

    def left_clicked(self, event):
        if self.is_mine:
            self.btn_obj.config(bg="HotPink4")
            sys.exit()
        else:
            if self.surronded_mines_count == 0:
                for cell in self.surrounded_cell:
                    cell.show_cell()
            self.show_cell()
        
    def show_cell(self):
        """Shows the number of mines around a particular cell"""
        #if the cell is not open, then open the cell
        if not self.is_open:
            Cell.cell_count -= 1
            self.btn_obj.config(text=self.surronded_mines_count)
            if Cell.label_obj:
                Cell.label_obj.config(text=f"Cell counts{Cell.cell_count}")
            
            # if the cell is open, then close the cell 
            self.is_open = True

        # change the buttom face to system color if is right clicked
        self.btn_obj.config(bg="SystemButtonFace")

        # congrates the winner
        if Cell.cell_count == settings.CELL_MINES:
            print("Congratulations")
        

    def axis(self, x, y):
        """returns cell with a specific location"""
        for c in Cell.all:
            if c.x == x and c.y == y:
                return c

    @property
    def surrounded_cell(self):
        """ returns the surround cell for each cell clicked"""
        cells = [
                self.axis(self.x-1, self.y-1),
                self.axis(self.x, self.y-1),
                self.axis(self.x+1, self.y-1),
                self.axis(self.x-1, self.y),
                self.axis(self.x+1, self.y),
                self.axis(self.x-1, self.y+1),
                self.axis(self.x, self.y+1),
                self.axis(self.x+1, self.y+1),
                ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surronded_mines_count(self):
        count = 0
        for cell in self.surrounded_cell:
            if cell.is_mine:
                count += 1
        return count


    def right_clicked(self, event):
        if self.cell_mine:
            self.btn_obj.config(bg="indian red")
            self.cell_mine = False
        else:
            self.btn_obj.config(bg="SystemButtonFace")
            self.cell_mine = True
        

    
    @staticmethod
    def create_label_obj(location):
        """creates a label object for the game"""
        lbl = Label(
            location,
            width=25,
            height=5,
            text=f"Cell counts{Cell.cell_count}",
            font=("", 25)
        )

        Cell.label_obj = lbl

    @staticmethod
    def randomise_cell():
        """change the value for is_mine for the selected cell"""
        picked_cell = random.sample(Cell.all, settings.CELL_MINES)
        for pick in picked_cell:
            pick.is_mine = True


    def __repr__(self) -> str:
        return f"Cell({self.x},{self.y})"