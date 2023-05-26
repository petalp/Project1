import tkinter as tk
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox


bg_color = "#6C6CA6"
fg_color = "white"

def clear_item():
    qty_spinbox.delete(0, tk.END)
    qty_spinbox.insert(0, 1)
    description_entry.delete(0, tk.END)
    price_spinbox.delete(0, tk.END)
    price_spinbox.insert(0, "0.0")

invoice_list = []
def add_item():
    qty = int(qty_spinbox.get())
    desc = description_entry.get()
    price = float(price_spinbox.get())
    line_total = qty*price
    invoice_item = [qty, desc, price, line_total ]

    tree.insert("", 0, values=invoice_item)
    clear_item()

    invoice_list.append(invoice_item)

def new_invoice():
    first_name_entry.delete(0, tk.END)
    last_name_enrty.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()

def generate_invoice():
    doc = DocxTemplate("project3/invoice_gen.docx")
    name = f"{first_name_entry.get()} {last_name_enrty.get()}"
    phone = phone_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
    salestax = 0.1
    total = subtotal*(1-salestax)
    doc.render({
                "name":name,
                "phone":phone,
                "invoice_list":invoice_list,
                "subtotal":subtotal,
                "salestax":f"{str(salestax*100)}%",
                "total":total})
    dtime = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    doc_name = f"project3/new_invoce {name} {dtime}.docx"

    doc.save(doc_name)
    messagebox.showinfo("Invoice complete", "Invoice Complete")

    new_invoice()

window = tk.Tk()
window.title("Invoice Generator Form")
window.resizable(False, False)
window.configure(bg="#4A4A70")



frame = tk.Frame(window, bg="#4A4A70") 
frame.pack(padx=100, pady=20)

first_name_label = tk.Label(frame, text="First Name",font=("", 20),fg=fg_color, bg=bg_color)
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(frame, text="Last Name",font=("", 20),fg=fg_color, bg=bg_color)
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(frame ,font=("", 20),fg=fg_color , bg=bg_color)
first_name_entry.grid(row=1, column=0)
last_name_enrty = tk.Entry(frame, font=("", 20),fg=fg_color , bg=bg_color)
last_name_enrty.grid(row=1, column=1)

phone_label = tk.Label(frame, text="Phone",font=("", 20),fg=fg_color, bg=bg_color)
phone_label.grid(row=0, column=2)
phone_entry = tk.Entry(frame,font=("", 20),fg=fg_color , bg=bg_color)
phone_entry.grid(row=1, column=2)

qty_label = tk.Label(frame, text="Qty",font=("", 20),fg=fg_color, bg=bg_color)
qty_label.grid(row=2, column=0)
qty_spinbox = tk.Spinbox(frame,from_=1,to="infinity",font=("", 20))
qty_spinbox.grid(row=3, column=0)

descripiton_label = tk.Label(frame, text="Description",font=("", 20),fg=fg_color,bg=bg_color)
descripiton_label.grid(row=2, column=1)
description_entry = tk.Entry(frame,font=("", 20),fg=fg_color , bg=bg_color)
description_entry.grid(row=3, column=1)

price_label = tk.Label(frame, text="Unit Price",font=("", 20),fg=fg_color, bg=bg_color)
price_label.grid(row=2, column=2)
price_spinbox = tk.Spinbox(frame, from_="0.0", to="infinity",bg=bg_color, font=("", 20) )
price_spinbox.grid(row=3, column=2)


add_button = tk.Button(frame, text="Add Item",font=("", 20),fg=fg_color, bg=bg_color, command=add_item)
add_button.grid(row=4, column=2)

columns = ("qty", "desc", "price", "total")
tree = ttk.Treeview(frame, columns=columns, show="headings",)
tree.heading("qty", text="Qty",)
tree.heading("desc", text="Description")
tree.heading("price", text="Unit Price")
tree.heading("total", text="Total")


tree.grid(row=5, column=0, columnspan=3, padx=100, pady=20)

save_invoice_button = tk.Button(frame, text="Generate Invoice",font=("", 20),fg=fg_color, bg=bg_color, command=generate_invoice)
save_invoice_button.grid(row=6, column=0, columnspan=3, sticky="news", padx=20, pady=5)
new_invoice_button = tk.Button(frame,text="New Invoice",font=("", 20),fg=fg_color, bg=bg_color, command=new_invoice)
new_invoice_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)
# run the form
window.mainloop()