import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

bg_color = "honeydew4"
text_bg = "#F0F0FF"
font = ("Mangeto", 30)
disx1 =  50

def register_form():
    """this form connect the database"""
    if firstNameEntry.get=="" or lastNameEntry=="" or contactNumberEntry.get()==""\
    or emailEntry.get() =="" or securityQuestCom.get()=="" or answerEntry.get()==""\
    or passwordEntry.get() =="" :
        messagebox.showerror("Error", "All fields must be filled")
        
    elif passwordEntry.get() != confirmPasswordEntry.get():
        messagebox.showerror("Error", "password do match")

    elif terms.get() == 0:
        messagebox.showerror("Error", "Terms and condition must be agreed")
    else:
        connect = pymysql.connect(host="127.0.0.1", user="root",password="jamestoma@123",database="students")
        cur = connect.cursor()
        cur.execute("select * from student_1 where email=%s",emailEntry.get())
        row = cur.fetchone()
        if row != None:
            messagebox.showerror("Error", "user already exist")
        else:
            cur.execute("insert into student_1(firstName,lastName,contactNumber,email,securityQuestion,answer,password)values(%s,%s,%s,%s,%s,%s,%s)",
                        (firstNameEntry.get(),lastNameEntry.get(),contactNumberEntry.get(),emailEntry.get(),securityQuestCom.get(),answerEntry.get(),passwordEntry.get()))
            connect.commit()
            messagebox.showinfo("Registration success!")

def login_form():
    window.destroy()
    import login




# create the tkinter window
window  = tk.Tk()
window.geometry("1500x900")
window.title("Registration form")

# background for the window
bg_img = tk.PhotoImage(file="general_pro/images/background_image.png")
label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0,y=0)
frame = tk.Frame(window, height=900, width=900, bg="#F0F0FF")
frame.place(x=600, y=0)


# student information
reg_title = tk.Label(frame, text="REGISTRATION FORM", font=("Georgina",35, "bold"), bg=text_bg)
reg_title.place(x=0, y=0)
firstName = tk.Label(frame, text="First Name", font=font, bg=text_bg)
firstName.place(x=disx1, y= 100)
lastName = tk.Label(frame, text="Last Name", font=font, bg=text_bg)
lastName.place(x=500, y= 100)
firstNameEntry = tk.Entry(frame, bg=bg_color, font=font, width=15)
firstNameEntry.place(x=disx1, y=150)
lastNameEntry = tk.Entry(frame, bg=bg_color, font=font, width=15)
lastNameEntry.place(x=500, y=150)
contactNumber = tk.Label(frame, text="Contact Number", font=font, bg=text_bg)
contactNumber.place(x=disx1, y=250)
email = tk.Label(frame, text="Email", font=font, bg=text_bg)
email.place(x=500, y=250)
contactNumberEntry = tk.Entry(frame, font=font, bg=bg_color, width=15)
contactNumberEntry.place(x=disx1, y=300)
emailEntry = tk.Entry(frame, font=font, bg=bg_color, width=15)
emailEntry.place(x=500, y=300)
securityQuest = tk.Label(frame, text="Security Question", font=font, bg=text_bg)
securityQuest.place(x=disx1, y=370)
answer = tk.Label(frame, text="Answer", font=font, bg=text_bg)
answer.place(x=500, y=370)
securityQuestCom = ttk.Combobox(frame, font=("", 20), width=20, )
securityQuestCom['values'] = ("select","What is your nick name?", 
                                "What is your best friend name",
                                "You birth place",
                                "Your favorite team",
                                "What is the name of favorite pet",
                                )
securityQuestCom.current(0)
securityQuestCom.place(x=disx1, y=420)
answerEntry = tk.Entry(frame, font=font, bg=bg_color, width=15)
answerEntry.place(x=500, y=420)

password = tk.Label(frame, text="Password", font=font, bg=text_bg)
password.place(x=disx1, y=500)
confirmPassword = tk.Label(frame, text="Confirm Password", font=font, bg=text_bg)
confirmPassword.place(y=500, x=500)
passwordEntry = tk.Entry(frame, font=font, bg=bg_color,width=15, show="*")
passwordEntry.place(x=disx1, y=550)
confirmPasswordEntry = tk.Entry(frame, font=font, bg=bg_color,width=15, show="*")
confirmPasswordEntry.place(x=500, y=550)

terms = tk.IntVar()
terms_cond = tk.Checkbutton(frame, text="Agree with terms and condition",onvalue=1, offvalue=0,
                        variable=terms,font=font, bg=text_bg)
terms_cond.place(x=disx1, y=700)
btn_img = tk.PhotoImage(file="general_pro/images/button.png")
button = tk.Button(frame, image=btn_img, bg=text_bg, cursor="hand2", command=register_form)
button.place(x=350, y=800)

login_img = tk.PhotoImage(file="general_pro/images/login_.png")
login_button = tk.Button(window,image=login_img, command=login_form)
login_button.place(x=150,y=300)


window.mainloop()