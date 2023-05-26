import tkinter as tk
import tkinter.ttk as tkk
from docxtpl import DocxTemplate
import datetime

bg_color1 = "#8B8B45"
bg_color2 = "#999932"    

font = ("", 20)

def clear_item():
    quantity_entry.delete(0, tk.END)
    quantity_entry.insert(0, "1")
    description_entry.delete(0, tk.END)
    unit_price_spinbox.delete(0, tk.END)
    unit_price_spinbox.insert(0, "0.0")

list_invoice = []
def additems():
    quantity = int(quantity_entry.get())
    desc = description_entry.get()
    unt_price = float(unit_price_spinbox.get())
    total = float(round(quantity * unt_price, 4))
    list_invoice.append([quantity, desc, unt_price, total])

    tree.insert("", 0, values=[quantity, desc, unt_price, total])

    clear_item()

def new_invoice():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

    clear_item()

    tree.delete(*tree.get_children())
    list_invoice.clear()


def gen_invoice():
    """This functoin generates the invoice and save it in world document"""
    doc = DocxTemplate("project3/invoice_gen.docx")
    name = first_name_entry.get() + last_name_entry.get()
    phone = phone_entry.get()
    lst_invoice = list_invoice
    subtotal = sum(item[3] for item in lst_invoice)
    subtax = 0.1
    total = subtotal * (1-subtax)

    doc.render(
        {"name":name,
        "phone":phone,
        "invoice_list":lst_invoice,
        "subtotal":subtotal,
        "salestax":f"{str(subtax*100)}%",
        "total":total}
        )
    dtime = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    doc_name = f"new_invoce {name} {dtime}.docx"
    doc.save(doc_name)
    new_invoice()


# design the window for the invoice entry
window = tk.Tk()
window.title("Invoice Generator")


# create the frame
frame = tk.Frame(window, bg=bg_color1)
frame.grid(row=0, column=0)

first_name = tk.Label(frame, text="First Name:", font=font,bg=bg_color2)
first_name.grid(row=0, column=0)
last_name = tk.Label(frame, text="Last Name:", font=font,bg=bg_color2)
last_name.grid(row=0, column=1)
phone = tk.Label(frame, text="Phone Number:", font=font,bg=bg_color2)
phone.grid(row=0, column=2)

first_name_entry = tk.Entry(frame, font=font, bg=bg_color2)
first_name_entry.grid(row=1, column=0)
last_name_entry = tk.Entry(frame, font=font, bg=bg_color2)
last_name_entry.grid(row=1, column=1)
phone_entry = tk.Entry(frame, font=font, bg=bg_color2)
phone_entry.grid(row=1, column=2)

quantity = tk.Label(frame, text="Qty:", font=font,bg=bg_color2)
quantity.grid(row=2, column=0)
description = tk.Label(frame, text="Description:", font=font,bg=bg_color2)
description.grid(row=2, column=1)
unity_price = tk.Label(frame, text="Unity price:", font=font,bg=bg_color2)
unity_price.grid(row=2, column=2)

quantity_entry = tk.Spinbox(frame,from_=0, to="infinity",font=font, bg=bg_color2)
quantity_entry.grid(row=3, column=0)
description_entry = tk.Entry(frame, font=font, bg=bg_color2)
description_entry.grid(row=3, column=1)
unit_price_spinbox = tk.Spinbox(frame, from_=0.0, to="infinity", font=font)
unit_price_spinbox.grid(row=3, column=2)

add_button = tk.Button(frame, text="Add items", font=font, bg=bg_color2, command=additems)
add_button.grid(row=4, column=2)

columns = ("qty", "desc","price", "total" )
tree = tkk.Treeview(frame,columns=columns,show="headings")
tree.heading("qty", text="Qty")
tree.heading("desc", text="Description")
tree.heading("price", text="Unity Price")
tree.heading("total", text="Total")
tree.grid(row=5, column=0, columnspan=4, padx=100, pady=30)

generate_invoice = tk.Button(frame, text="Generate Invoice", font=font, bg=bg_color2, command=gen_invoice)
generate_invoice.grid(row=6, column=0, columnspan=3, sticky="news", padx=100, pady=20)
new_invoice_button = tk.Button(frame, text="New Invoice", font=font, bg=bg_color2, command=new_invoice)
new_invoice_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=100, pady=20)


# run the window
window.mainloop()