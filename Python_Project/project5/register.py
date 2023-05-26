import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

lbl_font = ("", 35)
ent_font = ("", 25)
bg_color = "gray"

def clear():
    firstName_entry.delete(0, tk.END)
    lastName_entry.delete(0, tk.END)
    cont_num_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    question_lbl_combx.delete(0, tk.END)
    answer_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    psswd_confirm_entry.delete(0, tk.END)
    terms.set(0)

def login_form():
    window.destroy()
    import login

def register():
    if firstName_entry.get()=="" or lastName_entry.get()=="" or cont_num_entry.get()==""\
        or email_entry.get()=="" or question_lbl_combx.get()=="" or answer_entry.get()=="" or password_entry.get()=="" \
        or psswd_confirm_entry.get()=="":
        messagebox.showerror("Error", "Field must fill")
    
    elif password_entry.get() != psswd_confirm_entry.get():
        messagebox.showerror("Error", "password do not match")
    
    elif terms.get() == 0:
        messagebox.showerror("Error", "Terms and condition must be agreed")

    else:
        try:
            conn = pymysql.connect(host="127.0.0.1", user="root",password="jamestoma@123",database="students")
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM student WHERE email=%s",email_entry.get())
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "user all exist")
            else:
                cur.execute("INSERT INTO student (first_name, last_name,phonenumber, email, question, answer, password) Values(%s,%s,%s,%s,%s,%s,%s)",
                            (firstName_entry.get(), lastName_entry.get(),cont_num_entry.get(),email_entry.get(),question_lbl_combx.get(), answer_entry.get(),password_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration sucessful")
                clear()
                window.destroy()
                import login
        except Exception as e:
            messagebox.showerror("Error", f"{e}")


window = tk.Tk()
window.geometry("1708x1000")
window.title("Registration Form")
window.resizable(False, False)

bgimage = tk.PhotoImage(file="project5/images/background_image.png")
bgLabel = tk.Label(window, image=bgimage)
bgLabel.place(x=0, y=0)

reg_frame = tk.Frame(window, width=1000, height=950, bg=bg_color)
reg_frame.place(x=600, y=30)

# registration title
reg_title = tk.Label(reg_frame, text="Regisration Form", font=("", 40), bg=bg_color)
reg_title.place(x=0, y=0)

firstName = tk.Label(reg_frame, text="First Name", font=lbl_font, bg=bg_color)
firstName.place(x=130, y=130)
lastName = tk.Label(reg_frame, text="Last Name", font=lbl_font, bg=bg_color)
lastName.place(x=600, y=130)
firstName_entry = tk.Entry(reg_frame, font=ent_font, bg=bg_color)
firstName_entry.place(x=130, y=200)
lastName_entry = tk.Entry(reg_frame, font=ent_font, bg=bg_color)
lastName_entry.place(x=600, y=200)

contact_Number = tk.Label(reg_frame, text="Contact Number", font=lbl_font, bg=bg_color)
contact_Number.place(x=130, y=300)
email = tk.Label(reg_frame, text="Email", font=lbl_font, bg=bg_color)
email.place(x=600, y=300)
cont_num_entry = tk.Entry(reg_frame, font=ent_font, bg=bg_color)
cont_num_entry.place(x=130, y=370)
email_entry = tk.Entry(reg_frame, font=ent_font, bg=bg_color)
email_entry.place(x=600, y=370)

question_lbl = tk.Label(reg_frame, text="Security Question", font=lbl_font, bg=bg_color)
question_lbl.place(x=130, y= 450)
answer_lbl = tk.Label(reg_frame, text="Answer", font=lbl_font, bg=bg_color)
answer_lbl.place(x=600, y=450)
question_lbl_combx = ttk.Combobox(reg_frame, font=ent_font)

question_lbl_combx['values'] = ("select","What is your nick name?", 
                                "What is your best friend name",
                                "You birth place",
                                "Your favorite team",
                                "What is the name of favorite pet",
                                )
question_lbl_combx.current(0)

question_lbl_combx.place(x=130, y=520)
answer_entry = tk.Entry(reg_frame, font=ent_font, bg=bg_color)
answer_entry.place(x=600, y=520)

password = tk.Label(reg_frame, text="Password", font=lbl_font, bg=bg_color)
password.place(x=130, y=600)
confirm_psswrd = tk.Label(reg_frame, text="Confirm Password", font=lbl_font, bg=bg_color)
confirm_psswrd.place(x=600, y=600)
password_entry = tk.Entry(reg_frame, font=ent_font, bg=bg_color, show="*")
password_entry.place(x=130, y=670)
psswd_confirm_entry = tk.Entry(reg_frame, font=ent_font, bg=bg_color, show="*")
psswd_confirm_entry.place(x=600, y=670)

terms = tk.IntVar()
terms_cont = tk.Checkbutton(reg_frame, text="I Agree all the terms and condition",
                        variable=terms, onvalue=1, offvalue=0, font=lbl_font, bg=bg_color)
terms_cont.place(x=130, y=750)
bt_image = tk.PhotoImage(file="project5/images/button.png")
button = tk.Button(reg_frame, image=bt_image, bd=0, bg=bg_color, command=register)
button.place(x=400, y=850)

login_image = tk.PhotoImage(file="project5/images/login_.png")
button_login = tk.Button(window, image=login_image, command=login_form)
button_login.place(x=50, y=300)



window.mainloop()