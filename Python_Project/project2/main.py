import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



# background color for the data entry
bg_color1 = "#8B8B88"
bg_color2 = "#C2C2C2"
font = ("", 20)

def enter_data():
    """Retrieve the student info"""
    if terms_var.get() == "Accepted":
        # personal info
        reg_num = stu_reg_entry.get()
        if reg_num:
            title = stu_title_entry.get()
            first_name = first_name_entry.get()
            middle_name = middle_name_entry.get()
            last_name = last_name_entry.get()
            age = age_value.get()
            nationality = nation_value.get()
            sex = sex_entry.get()

            # course info
            register = reg_var.get()
            courses = course_value.get()
            semester = semester_value.get()
            dept = dept_entry.get()
            faculty = faculty_entry.get()


            print(f"Registration Number: {reg_num}")
            print(f"Name: {title}.{first_name} {middle_name} {last_name}")
            print(f"Age:{age} Sex: {sex} Nationality:{nationality}")
            print(f"No of courses:{courses} No of semester:{semester}")
            print(f"Department:{dept.title()} Faculty: {faculty.title()} \nRegistration:{register}")
            print("-----"*5)
        else:
            tk.messagebox.showwarning(title="Invalid Reg Num", message="Enter reg number")
    else:
        tk.messagebox.showwarning(title="Terms policy", message="Agree terms and condition")
# create entry data window 
window = tk.Tk()
window.resizable(False, False)

# create frame 
frame = tk.Frame(window, bg=bg_color1)
frame.grid(row=0, column=0)

# create label frame for the student information
student_info = tk.LabelFrame(frame,text="Student Infromation",  bg=bg_color2, font=font)
student_info.grid(row=0, column=0)
stu_reg_number = tk.Label(student_info, text="Reg Number:", font=font, bg=bg_color2)
stu_reg_number.grid(row=0, column=0)
stu_title_label = tk.Label(student_info, text="Title", font=font, bg=bg_color2)
stu_title_label.grid(row=0, column=1)
stu_reg_entry = tk.Entry(student_info, font=font, bg=bg_color2)
stu_reg_entry.grid(row=1, column=0)
stu_title_entry = ttk.Combobox(student_info, values=["", "Mr", "Mrs", "Miss"],font=font)
stu_title_entry.grid(row=1, column=1)

first_name = tk.Label(student_info, text="First Name", font=font, bg=bg_color2)
first_name.grid(row=2, column=0)
Middle_name = tk.Label(student_info, text="Middle Name", font=font, bg=bg_color2)
Middle_name.grid(row=2, column=1)
Last_name = tk.Label(student_info, text="Last Name", font=font, bg=bg_color2)
Last_name.grid(row=2, column=2)

first_name_entry = tk.Entry(student_info, font=font, bg=bg_color2)
first_name_entry.grid(row=3, column=0)
middle_name_entry = tk.Entry(student_info, font=font, bg=bg_color2)
middle_name_entry.grid(row=3, column=1)
last_name_entry = tk.Entry(student_info, font=font, bg=bg_color2)
last_name_entry.grid(row=3, column=2)

age = tk.Label(student_info, text="Age", font=font, bg=bg_color2)
age.grid(row=4, column=0)
nationality = tk.Label(student_info, text="Nationality", font=font, bg=bg_color2)
nationality.grid(row=4, column=1)
sex = tk.Label(student_info, text="Sex", font=font, bg=bg_color2)
sex.grid(row=4, column=2)

age_value = tk.Spinbox(student_info, from_=1, to=50, font=font)
age_value.grid(row=5, column=0)
nation_value =  ttk.Combobox(student_info, 
                        values=["Africa", "Asia", "Australia", "North America", "South America"],
                        font=("", 20))
nation_value.grid(row=5, column=1)
sex_entry = tk.Entry(student_info, font=font, bg=bg_color2)
sex_entry.grid(row=5, column=2)

for child in student_info.winfo_children():
    child.grid(padx=80, pady=10)


# create course information for the student
course_info = tk.LabelFrame(frame,text="Course Infromation", bg=bg_color2, font=font)
course_info.grid(row=1, column=0, sticky="news")

register = tk.Label(course_info , text="Registration", font=font, bg=bg_color2)
register.grid(row=0, column=0)
course_number = tk.Label(course_info , text="No. of courses", font=font, bg=bg_color2)
course_number.grid(row=0, column=1)
semester = tk.Label(course_info , text="No. of Semester", font=font, bg=bg_color2)
semester.grid(row=0, column=2)

reg_var = tk.StringVar(value="Not Registered")
register_stu = tk.Checkbutton(course_info, text="Registered", font=font,bg=bg_color2, variable=reg_var,
                            onvalue="Registered", offvalue="Not Registered")

register_stu.grid(row=1, column=0)
course_value = tk.Spinbox(course_info, from_=1, to=50, font=font)
course_value.grid(row=1, column=1)
semester_value = tk.Spinbox(course_info, from_=1, to=50, font=font)
semester_value.grid(row=1, column=2)

department = tk.Label(course_info , text="Department", font=font, bg=bg_color2)
department.grid(row=2, column=0)
faculty = tk.Label(course_info , text="Faculty", font=font, bg=bg_color2)
faculty.grid(row=2, column=1)

dept_entry = tk.Entry(course_info, font=font, bg=bg_color2)
dept_entry.grid(row=3, column=0)
faculty_entry = tk.Entry(course_info, font=font, bg=bg_color2)
faculty_entry.grid(row=3, column=1)

for child in course_info.winfo_children():
    child.grid(padx=80, pady=10)

# Terms and condition for the student
terms_frame = tk.LabelFrame(frame, bg=bg_color2, text="Terms and Condition",font=font)
terms_frame.grid(row=2, column=0,sticky="news")
terms_var = tk.StringVar(value="Not Accepted")
terms_stu = tk.Checkbutton(terms_frame, text="Terms and Condition", font=font,bg=bg_color2, 
                            variable=terms_var, onvalue="Accepted", offvalue="Not Accepted")
terms_stu.grid(row=0, column=0)


button = tk.Button(frame, text="Enter", font=font, bg=bg_color2, command=enter_data)
button.grid(row=3, column=0, sticky="news")

for child in frame.winfo_children():
    child.grid( pady=10)

window.mainloop()