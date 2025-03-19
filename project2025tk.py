import tkinter
import ttkbootstrap as ttk
import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector
#import psycopg2 as pg2



def form():
    def exit():
        application_form_window.destroy()
    def submit():
        data = (0, entrylastname.get().upper(), entryfirstname.get().upper(), entrymiddlename.get().upper(),
                entrybirthdate.get().upper(), entrycity.get().upper(), entrybrgy.get().upper(), entrystreet.get().upper(),
                entryphonenubmer.get().upper(), entrysss.get().upper(), entrypagibig.get().upper(), entryphilhealth.get().upper(),
                entryemergencynumber.get().upper(), entryemergencyname.get().upper(), entrydatehired.get().upper())

        db = mysql.connector.connect(host="localhost",user='root',password='nanay123',db = 'project2025')
        cursor = db.cursor()
        mysqlquery = ("INSERT INTO project2025.employees(emp_id,last_name,first_name,middle_name,birth_date,city,barangay,street,phone_number,sss_number,pagibig_number,philhealth_number,emergency_number,emergency_name,date_hired) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(mysqlquery, data)
        db.commit()



        #lastname = entrylastname.get()
        #firstname = entryfirstname.get()
        #middlename = entrymiddlename.get()
        #birthdate = entrybirthdate.get()
        #city = entrycity.get()
        #brgy = entrybrgy.get()
        #street = entrystreet.get()
        #phonenumber = entryphonenubmer.get()
        #sssnumber = entrysss.get()
        #pagibignumber = entrypagibig.get()
        #philhealthnumber = entryphilhealth.get()
        #emergencynumber = entryemergencynumber.get()
        #emergencyname = entryemergencyname.get()
        #datehired = entrydatehired.get()
        print(data)





        entrylastname.delete(0, 'end')
        entryfirstname.delete(0,'end')
        entrymiddlename.delete(0,'end')
        entrybirthdate.delete(0, 'end')
        entrycity.delete(0, 'end')
        entrybrgy.delete(0, 'end')
        entrycity.delete(0, 'end')
        entrystreet.delete(0, 'end')
        entryphonenubmer.delete(0, 'end')
        entrysss.delete(0, 'end')
        entrypagibig.delete(0, 'end')
        entryphilhealth.delete(0, 'end')
        entryemergencyname.delete(0, 'end')
        entryemergencynumber.delete(0, 'end')
        entrydatehired.delete(0, 'end')





    application_form_window = ttk.Frame(window,style='light')
    application_form_window.place(x=0,y=0,width=1000,height=600)



    form_frame = ttk.Labelframe(application_form_window,text="PERSONAL INFORMATION")
    form_frame.place(x=200,y=100,width=600,height=350)



    # LAST NAME
    labellastname = ttk.Label(form_frame,text="LAST NAME")
    labellastname.place(x=70,y=10)
    entrylastname= ttk.Entry(form_frame)
    entrylastname.place(x=70, y=25,width=190,height=25)
    # FIRST NAME
    labelfirstname = ttk.Label(form_frame, text="FIRST NAME")
    labelfirstname.place(x=70, y=50)
    entryfirstname = ttk.Entry(form_frame)
    entryfirstname.place(x=70, y=65, width=190, height=25)
    #MIDDLE NAME
    labelmiddlename = ttk.Label(form_frame, text="MIDDLE NAME")
    labelmiddlename.place(x=70, y=90)
    entrymiddlename = ttk.Entry(form_frame)
    entrymiddlename.place(x=70, y=105, width=190, height=25)
    #BIRTHDATE
    labelbirthdate = ttk.Label(form_frame, text="BIRTH DATE")
    labelbirthdate.place(x=70, y=130)
    entrybirthdate = ttk.Entry(form_frame)
    entrybirthdate.place(x=70, y=145, width=190, height=30)
    #CITY
    labelcity = ttk.Label(form_frame, text="CITY")
    labelcity.place(x=70, y=170)
    entrycity = ttk.Entry(form_frame)
    entrycity.place(x=70, y=185, width=190, height=25)


    # BRGY
    labelbrgy = ttk.Label(form_frame, text="BARANGAY")
    labelbrgy.place(x=70, y=210)
    entrybrgy = ttk.Entry(form_frame)
    entrybrgy.place(x=70, y=225, width=190, height=25)

    # STREET
    labelstreet = ttk.Label(form_frame, text="STREET")
    labelstreet.place(x=70, y=250)
    entrystreet = ttk.Entry(form_frame)
    entrystreet.place(x=70, y=265, width=190, height=25)


    #PHONE NUMBER
    labelphonenumber = ttk.Label(form_frame, text="PHONE NUMBER")
    labelphonenumber.place(x=320, y=10)
    entryphonenubmer = ttk.Entry(form_frame)
    entryphonenubmer.place(x=320, y=25, width=190, height=25)

    # SSS NUMBER
    labelsss = ttk.Label(form_frame, text="SSS NUMBER")
    labelsss.place(x=320, y=50)
    entrysss = ttk.Entry(form_frame)
    entrysss.place(x=320, y=65, width=190, height=25)

    # PAG IBIG NUMBER
    labelpagibig = ttk.Label(form_frame, text="PAG IBIG")
    labelpagibig.place(x=320, y=90)
    entrypagibig = ttk.Entry(form_frame)
    entrypagibig.place(x=320, y=105, width=190, height=25)

    # PHILHEALTH
    labelphilhealth = ttk.Label(form_frame, text="PHILHEALTH")
    labelphilhealth.place(x=320,y=130)
    entryphilhealth = ttk.Entry(form_frame)
    entryphilhealth.place(x=320, y=145, width=190, height=25)

    # EMERGENCY NUMBER
    labelemergencynumber = ttk.Label(form_frame, text="EMERGENCY NUMBER")
    labelemergencynumber.place(x=320, y=170)
    entryemergencynumber = ttk.Entry(form_frame)
    entryemergencynumber.place(x=320, y=185, width=190, height=25)

    # EMERGENCY NAME
    labelemergencyname = ttk.Label(form_frame, text="EMERGENCY NAME")
    labelemergencyname.place(x=320, y=210)
    entryemergencyname = ttk.Entry(form_frame)
    entryemergencyname.place(x=320, y=225, width=190, height=25)

    # DATE HIRED
    labeldatehired = ttk.Label(form_frame, text="DATE HIRED")
    labeldatehired.place(x=320, y=250)
    entrydatehired = ttk.Entry(form_frame)
    entrydatehired.place(x=320, y=265, width=190, height=35)

    # BUTTON ------------------------------------------------------------------------------
    exitbutton = ttk.Button(application_form_window,image=EXIT,command=exit,style='light')
    exitbutton.place(x=0,y=0,width=100,height=100)

    submitbutton = ttk.Button(application_form_window, image=SUBMIT, command=submit, style='light')
    submitbutton.place(x=450, y=450, width=100, height=100)



    # BUTTON/ /////////////////////////////////////////////////////////////////////////////////

def assign():
    def submit():
        data = (emp_id_assign.get(),position.get())
        db = mysql.connector.connect(host="localhost", user='root', password='nanay123', db='project2025')
        cursor = db.cursor()
        cursorquery = "INSERT INTO project2025.emp_position(emp_id,position)VALUES(%s,%s)"
        cursor.execute(cursorquery,data)
        db.commit()
        emp_id_assign.delete(0,"end")
        position.delete(0,'end')


    def exit():
        assign_frame.destroy()

    list = ["Data Analyst","Senior Data Analyst","CEO","Customer Service","Encoder",
            "I.T STAFF","Janitor","House Keeping", "Merchandiser","Merchandising Coordinator",
            "Tactical Coordinator","Roving Merchandiser","Driver","Helper",
            "Receiving Supervisor","Checker","Warehouseman","Warehouse Supervisor","Accounting",
            "Assistant Accounting","Collector","Admin"]


    assign_frame = ttk.Frame(window,style='light')
    assign_frame.place(x=0,y=0,width=1000,height=600)

    assign_form_frame = ttk.Labelframe(assign_frame, text="JOB POSITION",style='light')
    assign_form_frame.place(x=200, y=100, width=600, height=350)


    emp_id_assign_label = ttk.Label(assign_form_frame,text="Employee I.D ").place(x=250,y=150)
    emp_id_assign = ttk.Entry(assign_form_frame)
    emp_id_assign.place(x=200,y=170,width=200,height=30)

    position_label = ttk.Label(assign_form_frame, text="Position").place(x=270, y=200)
    position = ttk.Combobox(assign_form_frame,values=list,style='readonly')
    position.place(x=200,y=220,width=200,height=50)









    #------------------------------- BUTTON -------------------------------------#
    exitbutton = ttk.Button(assign_frame,style='light',image=EXIT,command=exit)
    exitbutton.place(x=0,y=0,width=100,height=100)

    submitbutton = ttk.Button(assign_form_frame, image=SUBMIT, command=submit, style='light')
    submitbutton.place(x=250, y=50, width=100, height=100)



    #------------------------------- BUTTON -------------------------------------#


def salary():

    def submit():
        data = (emp_id.get(), salary.get(),datesalary.get())
        db = mysql.connector.connect(host="localhost", user='root', password='nanay123', db='project2025')
        cursor = db.cursor()
        cursorquery = "INSERT INTO project2025.salary_history(emp_id,salary,payout_date)VALUES(%s,%s,%s)"
        cursor.execute(cursorquery, data)
        db.commit()

        emp_id.delete(0,'end')
        salary.delete(0,'end')
        datesalary.delete(0,'end')
        print("Nihao Ma")

    def exit():
        salary_frame.destroy()


    salary_frame = ttk.Frame(window, style='light')
    salary_frame.place(x=0, y=0, width=1000, height=600)

    salary_form_frame = ttk.Labelframe(salary_frame, text="JOB POSITION",style='light')
    salary_form_frame.place(x=200, y=100, width=600, height=350)

    salary_assign_label = ttk.Label(salary_form_frame, text="EMPLOYEE I.D ").place(x=250, y=150)
    emp_id = ttk.Entry(salary_form_frame)
    emp_id.place(x=200, y=170, width=200, height=30)

    salary_label = ttk.Label(salary_form_frame, text="SALARY").place(x=270, y=200)
    salary = ttk.Entry(salary_form_frame, style="success")
    salary.place(x=200, y=220, width=200, height=30)

    date_label = ttk.Label(salary_form_frame, text="DATE").place(x=270, y=250)
    datesalary = ttk.Entry(salary_form_frame, style="success")
    datesalary.place(x=200, y=270, width=200, height=30)

    # ------------------------------- BUTTON -------------------------------------#
    exitbutton = ttk.Button(salary_frame, style='light', image=EXIT, command=exit)
    exitbutton.place(x=0, y=0, width=100, height=100)

    submitbutton = ttk.Button(salary_form_frame, image=SUBMIT, command=submit, style='light')
    submitbutton.place(x=250, y=50, width=100, height=100)


window = ttk.Window()
window.geometry("1000x600")
window.title("PROJECT 2025")
window.resizable(False,False)

#LOGO - - - -- - - - - - - - -- - - - - - - - -- - - - - - - -- - - -

#APPLICATION
application = (Image.open("logo/resume-removebg-preview.png"))
resize_application = application.resize((100,100),Image.ADAPTIVE)
APPLICATION = ImageTk.PhotoImage(resize_application)


#ASSIGN EMP
assignemp = (Image.open("logo/assign_employee.png"))
resize_assignemp = assignemp.resize((100,100),Image.ADAPTIVE)
ASSIGN = ImageTk.PhotoImage(resize_assignemp)

# SALARY HISTORY
salary_history = (Image.open("logo/salary history.png"))
resize_salary_history = salary_history.resize((100,100),Image.ADAPTIVE)
SALARY_HISTORY = ImageTk.PhotoImage(resize_salary_history)

#CRUD EMPLOYEE
search_emp = (Image.open("logo/search_employee.png"))
resize_search_emp = search_emp.resize((100,100),Image.ADAPTIVE)
SEARCH = ImageTk.PhotoImage(resize_search_emp)











#EXIT
exit = (Image.open("logo/exit-full-screen-removebg-preview.png"))
resize_exit = exit.resize((80,80),Image.ADAPTIVE)
EXIT= ImageTk.PhotoImage(resize_exit)



# SUBMIT

#EXIT
submit = (Image.open("logo/submit-removebg-preview.png"))
submit_exit = submit.resize((80,80),Image.ADAPTIVE)
SUBMIT = ImageTk.PhotoImage(submit_exit)









# LOGO ````````````````````````````````````````````- -- - - - - - - - - - - -


#BUTTON

#BUTTON FOR APPLICATION
applicationbutton = ttk.Button(window,image=APPLICATION,style='outline-light',command=form)
applicationbutton.place(x=200,y=225,width=150,height=150)

#BUTTON FOR ASSIGN EMPLOYEES
assignbutton = ttk.Button(window,image=ASSIGN,style='outline-light',command=assign)
assignbutton.place(x=350,y=225,width=150,height=150)

#BUTTON FOR SALARY_HISTORY
salary_history_button = ttk.Button(window,image=SALARY_HISTORY,style='outline-light',command=salary)
salary_history_button.place(x=500,y=225,width=150,height=150)

#BUTTON FOR SEARCH/CRUD EMPLOYEES
search_button = ttk.Button(window,image=SEARCH,style='outline-light',command=form)
search_button.place(x=650,y=225,width=150,height=150)



window.mainloop()
