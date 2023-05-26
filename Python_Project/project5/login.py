from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk


bg_color = "white"
font = ("", 25)

def register_form():
    window.destroy()
    import register

def signin():
    if emailEntry.get() == "" or passwrdEntry.get() == "":
        messagebox.showerror("error", "All fields are required!")

    else:
        try:
            connect = pymysql.connect(host="127.0.0.1", user="root",password="jamestoma@123",database="students")
            cur = connect.cursor()
            cur.execute("select * from student where email=%s and password=%s",(emailEntry.get(), passwrdEntry.get()),)
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Ivalid Email or Password")
            else:
                messagebox.showinfo("Success", "Welcome")
            connect.close()
        except Exception as e:
            messagebox.showerror("error", f"Error is due to {e}")

def reset_password():
    if emailEntry.get() == "":
        messagebox.showerror("Error", "please enter the email address to reset your password")

    else:
        connect = pymysql.connect(host="127.0.0.1", user="root",password="jamestoma@123",database="students")
        cur = connect.cursor()
        cur.execute("select * from student where email=%s",emailEntry.get())
        row = cur.fetchone()
        if row == None:
            messagebox.showerror("Error", "Please enter the correct email address!")
        else:
            connect.close()

            def new_password():
                if securityCombox.get() == "select" or answerEntry.get()=="" or passwordEntry.get()=="":
                    messagebox.showerror("Error", "All fields are required")

                else:
                    con = pymysql.connect(host="127.0.0.1", user="root",password="jamestoma@123",database="students")
                    cur = con.cursor()
                    cur.execute("select * from student where email=%s and question=%s and answer=%s", (emailEntry.get(),
                                    securityCombox.get(), answerEntry.get()))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Security Question or Answer is Incorrect",parent=window_)
                    else:
                        cur.execute("update student set password=%s where email=%s",(passwordEntry.get(),emailEntry.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Password is reset, Please with password", parent=window_)
                        securityCombox.current(0)
                        answerEntry.delete(0, END)
                        passwordEntry.delete(0, END)
                        window_.destroy()
                        
            window_ = Toplevel()
            window_.title("Forget Password")
            window_.geometry("700x800+900+80")
            window_.config(bg="white")
            window_.focus_force()
            window_.grab_set()
            
            forgetLabel = Label(window_, text="Forget", font=("monospace", 40, "bold"), bg=bg_color)
            forgetLabel.place(x=128, y=20)

            passwordLabel = Label(window_, text="PassWord", font=("monospace", 40, "bold"), bg=bg_color, fg="green")
            passwordLabel.place(x=300, y=20)

            forgetPassImg = PhotoImage(file="project5/images/forget_passwd.png")
            forgetpasslbl = Label(window_, image=forgetPassImg, bg=bg_color)
            forgetpasslbl.place(x=200, y=150)

            securityqueslabel = Label(window_, text="Security Questions", font=("monospace", 40, "bold"), bg="white")
            securityqueslabel.place(x=128, y=320)
            securityCombox = ttk.Combobox(window_,font=font, state="readonly")
            securityCombox['values'] = ("select","what is your nick name?", 
                                        "what is your best friend name",
                                        "You birth place",
                                        "Your favorite team",
                                        "what is the name of favorite pet",
                                        )

            securityCombox.place(x=128, y=400)
            securityCombox.current(0)
            
            answerLabel = Label(window_, text="Answer", font=font, bg="white")
            answerLabel.place(x=128, y=450)
            answerEntry = Entry(window_, font=font, bg="gray", width=25)
            answerEntry.place(x=128, y=500)

            passwordLabel = Label(window_, text="New Password", font=font, bg="white")
            passwordLabel.place(x=128, y=550)
            passwordEntry = Entry(window_, font=font, bg="gray", width=25)
            passwordEntry.place(x=128, y=600)

            changeButton = Button(window_, text="Change Password",bg="green",font=font, fg="white",
                                activebackground="green", activeforeground="white", command=new_password)
            changeButton.place(x=200, y=720)


            window_.mainloop()

window = Tk()

window.geometry("1500x800+50+50")
window.title("Login Page")

bgloginimage = PhotoImage(file="project5/images/login_1.png")
bgloginLabel = Label(window, image=bgloginimage)
bgloginLabel.place(x=0, y=0)


frame = Frame(window, width=1200, height=600, bg=bg_color) 
frame.place(x=200, y=140)

userimage = PhotoImage(file="project5/images/user.png")
userimageLabel = Label(frame, image=userimage)
userimageLabel.place(x=100, y=150)

emailLbl = Label(frame, text="Email", bg=bg_color, font=font)
emailLbl.place(x=500, y=150)
emailEntry = Entry(frame, font=font, bg="gray")
emailEntry.place(x=500, y=200)

passwordlbl = Label(frame, text="Password",font=font, bg=bg_color)
passwordlbl.place(x=500, y=250)
passwrdEntry = Entry(frame, font=font, bg="gray", show="*")
passwrdEntry.place(x=500, y=300)

regbutton = Button(frame, text="Register New Account?", cursor="hand2", 
                font=font, bg=bg_color,bd=0, command=register_form)
regbutton.place(x=400, y=350)
forgetbtn = Button(frame, text="forget password?", cursor="hand2",activeforeground="red",
                fg="red", activebackground="white", font=font, bg=bg_color,bd=0,
                command=reset_password)
forgetbtn.place(x=800, y=350)

loginbttn = Button(window,text="Login", cursor="hand2",
                font=font, bg="gray20", fg="white",command=signin)
loginbttn.place(x=1000, y=600)


window.mainloop()