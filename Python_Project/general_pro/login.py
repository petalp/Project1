import tkinter as tk
from tkinter import messagebox
import pymysql
import tkinter.ttk as ttk

font = ("", 40)
font_text = ("", 30)
bg_color_entry = "#83838B"
bg_color = "honeydew"

def login_form():
    # checks if the email or password entry field is emtpy
    if email_entry.get() == "" or password_entry.get()=="":
        messagebox.showerror("Error", "Email or password is empty")
    else:
        try:
            connect = pymysql.connect(host="127.0.0.1", database="students",user="root",password="jamestoma@123")
            cur = connect.cursor()
            cur.execute("select * from student_1 where email=%s",email_entry.get())
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "User does not exist")
            else:
                messagebox.showinfo("Welcome", "Successful")
                connect.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {e}")

        
def reset_password():
    # check if the email field is empty
    if email_entry.get() == "":
        messagebox.showerror("Error","Please the enter email address to reset your password")
    else:
        connect = pymysql.connect(host="127.0.0.1", database="students",user="root",password="jamestoma@123")
        cur = connect.cursor()
        cur.execute("select * from student_1 where email=%s",email_entry.get())
        row = cur.fetchone()

        #check if the user enter a wrong email  address
        if row == None:
            messagebox.showerror("Error", "You have entered a wrong email address")
        else:
            connect.close()

            def new_password():
                # check for security questions, answer and new password
                if question_com.get()=="select" or answer_entry.get()=="" or new_password_entry.get()=="":
                    messagebox.showerror("Error", "field must not be empty", parent=window_top)
                else:
                    connect = pymysql.connect(host="127.0.0.1", database="students",user="root",password="jamestoma@123")
                    cur = connect.cursor()
                    cur.execute("select * from student_1 where email=%s and securityQuestion=%s and answer=%s",
                                (email_entry.get(), question_com.get(), answer_entry.get()))
                    row == cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "You have entered wrong information",parent=window_top)
                    else:
                        cur.execute("update student_1  set password=%s where email=%s",(new_password_entry.get(), email_entry.get()))
                        connect.commit()
                        connect.close()
                        messagebox.showinfo("Success", "Password Reset",parent=window_top)
                        question_com.current(0)
                        answer_entry.delete(0, tk.END)
                        new_password_entry.delete(0, tk.END)
                        window_top.destroy()

            window_top = tk.Toplevel()

            
            window_top.title("Forget password")
            window_top.geometry("600x800")
            window_top.config(bg="white")
            window_top.focus_force()
            window_top.grab_set()

            # interface title
            title_1 = tk.Label(window_top, text="Forget", font=font_text,bg="white")
            title_1.place(x=100, y=50)
            title_2 = tk.Label(window_top, text="PassWord", font=font_text, fg="green",bg="white")
            title_2.place(x=220, y=50)

            toplevel_img = tk.PhotoImage(file="general_pro/images/forget_passwd.png")
            lbl_img = tk.Label(window_top, image=toplevel_img)
            lbl_img.place(x=150, y=150)

            # ask security questions
            security_question = tk.Label(window_top, text="Security Questions", font=font_text,bg="white")
            security_question.place(x=100, y=350)
            question_com = ttk.Combobox(window_top, font=font_text)
            question_com['values'] = ("select","what is your nick name?", 
                                        "what is your best friend name",
                                        "You birth place",
                                        "Your favorite team",
                                        "what is the name of favorite pet",
                                        )
            question_com.place(x=100, y=400)
            question_com.current(0)

            answer_lbl = tk.Label(window_top, text="Answer", font=font_text,bg="white")
            answer_lbl.place(x=100,y=470)
            answer_entry = tk.Entry(window_top, font=font_text, bg="gray")
            answer_entry.place(x=100, y=520)
            new_password_lbl = tk.Label(window_top, text="New Password", font=font_text,bg="white")
            new_password_lbl.place(x=100,y=600)
            new_password_entry = tk.Entry(window_top, font=font_text, bg="gray")
            new_password_entry.place(x=100,y=650)

            reset_button = tk.Button(window_top,text="Reset Password",bg="green", fg="white", font=("", 20),command=new_password)
            reset_button.place(x=200, y=720)

            
    

            window_top.mainloop()

def register_form():
    window.destroy()
    import register

# create login window
window = tk.Tk()
window.geometry("1500x800")
window.title("Login")
window.resizable(False, False)

# create the background for the login interface
bk_img = tk.PhotoImage(file="general_pro/images/login_1.png")
lbl_bk = tk.Label(window, image=bk_img)
lbl_bk.place(x=0, y=0)

#create frame for the login interface
frame = tk.Frame(window, width=1300, height=700, bg=bg_color)
frame.place(x=100, y=50)
user_img = tk.PhotoImage(file="general_pro/images/user.png")
user_lbl = tk.Label(frame, image=user_img)
user_lbl.place(x=100, y=100)
email_lbl = tk.Label(frame, text="Email", font=font, bg=bg_color)
email_lbl.place(x=500, y=50)
email_entry = tk.Entry(frame, font=font_text, width=20,bg=bg_color_entry)
email_entry.place(x=500, y=120)
password_lbl = tk.Label(frame, text="Password", font=font, bg=bg_color)
password_lbl.place(x=500, y=180)
password_entry = tk.Entry(frame, font=font_text, width=20,bg=bg_color_entry)
password_entry.place(x=500, y=250)

register_button = tk.Button(frame, text="Register New Account?",bg=bg_color,activebackground=bg_color,
        font=font_text, bd=0, command=register_form)
register_button.place(x=350, y=350)
forget_button = tk.Button(frame, text="Forget password",bg=bg_color,
                fg="red",activebackground=bg_color, font=font_text, bd=0, command=reset_password)
forget_button.place(x=900, y=350)
login_button = tk.Button(frame, text="Login", font=font_text, bg="gray", fg="white", command=login_form)
login_button.place(x=700, y=450)

window.mainloop()