import tkinter as tk
from PIL import ImageTk
from numpy import random
import sqlite3



bg_color = "#B0B0C4"

# create the general window
root = tk.Tk()
root.title("Toma's Recipe")
root.eval("tk::PlaceWindow . center")
root.resizable(False, False)

# create first widget for the recipe
frame1 = tk.Frame(root, width=500, height=800, bg= bg_color)
frame2 = tk.Frame(root, bg= bg_color)
for frame in (frame1, frame2):
        frame.grid(row=0, column=0, sticky="nesw")


def clear_widgets(frame):
        for widgets in frame.winfo_children():
                widgets.destroy()

# get recipe from the database
def fetch_db():
        """Fetch recipe from the database"""
        connection = sqlite3.connect("venv/recipes.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")

        # select table random from the database
        all_table = cursor.fetchall()
        idx = random.randint(0, len(all_table)-1)
        table_name = all_table[idx][1]

        # select the ingredient from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        table_records = cursor.fetchall()
        
        # close the database 
        connection.close()
        return table_name, table_records

def pre_process(table_name, table_record):
        """Processes the table and record"""
        title = table_name[:-6]
        title = "".join([char if char.islower() else " " + char for char in title])
        
        #ingredient
        ingredients = []
        for i in table_record:
                name = i[1]
                qty = i[2]
                unit = i[3]
                ingredients.append(f"{qty} {unit} of {name}")
        
        return title, ingredients

def load_frame1():
        clear_widgets(frame2)
        """Designing frame1 for the recipe"""
        frame1.tkraise()
        frame1.pack_propagate(False)
        logo_img = ImageTk.PhotoImage(file="venv/RRecipe_logo.png")
        logo_widet = tk.Label(frame1, image=logo_img, bg=bg_color)
        logo_widet.image = logo_img
        logo_widet.pack()

        # display the widget message
        tk.Label(frame1,
                text="Are you ready for random recipe....",
                bg="#B0B0C4",
                fg="white",
                font=("TkHeadingFont", 20)
                ).pack()
        
        tk.Button(
                frame1,
                text="SHUFFLE",
                bg=bg_color,
                fg="White",
                font=("TkMenuFont", 20),
                cursor="hand2",
                activebackground="#FFFFA0",
                activeforeground="#9090EE",
                command=lambda:load_frame2()
        ).pack(pady=20)


def load_frame2():
        clear_widgets(frame1)
        """This function displays the recipe info"""
        frame2.tkraise()

        table_name,table_record= fetch_db()
        title, ingredients = pre_process(table_name, table_record)
        # display the recipe on the frame
        logo_img = ImageTk.PhotoImage(file="venv/RRecipe_logo_bottom.png")
        logo_widet = tk.Label(frame2, image=logo_img, bg=bg_color)
        logo_widet.image = logo_img
        logo_widet.pack()

        # display the title on the frame
        tk.Label(frame2,
                text=title,
                bg="#B0B0C4",
                fg="white",
                font=("TkHeadingFont", 20)
                ).pack()
        
        # display the ingredients on the frame
        for i in ingredients:
                # display the widget message
                tk.Label(frame2,
                        text=i,
                        bg="#B0B0C4",
                        fg="white",
                        font=("TkHeadingFont", 20)
                        ).pack()
        # display the back buttom on the frame
        tk.Button(
                frame2,
                text="BACK",
                bg=bg_color,
                fg="White",
                font=("TkMenuFont", 20),
                cursor="hand2",
                activebackground="#FFFFA0",
                activeforeground="#9090EE",
                command=lambda:load_frame1()
        ).pack(pady=10)

load_frame1()


# run the app
root.mainloop()