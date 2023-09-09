import configparser
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector
import pymysql
from PIL import Image, ImageTk

import credentials as cr


class home:
    def __init__(self, root):
        self.root = root
        self.root.title("HOME PAGE")
        self.root.geometry("1280x800+0+0")
        self.root.config(bg="white")
        self.lt = Label(self.root, text="Parking Management System", bg="#FCD12A", fg="white", bd=20,
                        font=("times new roman", 30, "bold"), padx=2, pady=6)

        self.lt.pack(side=TOP, fill=X)
        self.fr = Frame(self.root, bd=10, padx=10, bg="white")
        self.fr.place(x=0, y=100, width=250, height=600)
        self.b1 = Button(self.fr, height=5, width=25, bg="#3778C2", fg="white", bd=0, text="SLOT AVAILABILITY",
                         font=("times new roman", 13, "bold"), command=lambda: self.home_fun())
        self.b2 = Button(self.fr, height=5, width=25, bg="#E12B38", fg="white", bd=0, text="ADD VEHICLE",
                         font=("times new roman", 13, "bold"), command=lambda: self.vecy_fun())
        self.b3 = Button(self.fr, height=5, width=25, bg="#3EB650", fg="white", bd=0, text="MANAGE VEHICLE",
                         font=("times new roman", 13, "bold"), command=lambda: self.macy_fun())
        self.b4 = Button(self.fr, height=5, width=25, bg="#E56B1F", fg="white", bd=0, text="HISTORY",
                         font=("times new roman", 13, "bold"), command=lambda: self.hist_fun())
        self.b5 = Button(self.fr, height=5, width=25, bg="#FCC133", fg="white", bd=0, text="PAYMENT",
                         font=("times new roman", 13, "bold"), command=lambda: self.payment_fun())
        self.b1.place(x=0, y=5)
        self.b2.place(x=0, y=120)
        self.b3.place(x=0, y=230)
        self.b4.place(x=0, y=340)
        self.b5.place(x=0, y=450)
        self.fr = Frame(self.root, bg="black")
        self.fr.place(x=270, y=120, width=980, height=550)

        self.bg = ImageTk.PhotoImage(file="E:/GUI USING TKINTER/image/Parking-Management-System1.jpg")
        self.bg_image = Label(self.fr, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)

    def home_fun(self):
        connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
        cur = connection.cursor()
        cur.execute("select count(*) from managehistory;")
        global t1
        global slot
        slot=[]
        for i in cur:
            t1=i
        fr1 = Frame(self.root)
        fr1.place(x=270, y=120, width=980, height=550)
        b1 = Button(fr1, text="1", bg="green", height=7,command=lambda: self.myclick1(), width=31)
        b1.place(x=0, y=5)
        b2 = Button(fr1, text="2", padx=40, pady=20, bg="green", height=5, width=20)
        b2.place(x=0, y=120)
        b3 = Button(fr1, text="3", padx=40, pady=20, height=5, width=20, bg="green")
        b3.place(x=0, y=230)

        b4 = Button(fr1, text="4", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b4.place(x=0, y=340)
        b5 = Button(fr1, text="5", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b5.place(x=0, y=450)
        b6 = Button(fr1, text="6", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b6.place(
            x=250, y=5)
        b7 = Button(fr1, text="7", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b7.place(
            x=250, y=120)
        b8 = Button(fr1, text="8", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b8.place(
            x=250, y=230)
        b9 = Button(fr1, text="9", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b9.place(
            x=250, y=340)
        b10 = Button(fr1, text="10", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b10.place(
            x=250, y=450)
        b11 = Button(fr1, text="11", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b11.place(
            x=500, y=5)
        b12 = Button(fr1, text="12", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b12.place(
            x=500, y=120)
        b13 = Button(fr1, text="13", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b13.place(
            x=500, y=230)
        b14 = Button(fr1, text="14", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2")
        b14.place(
            x=500, y=340)
        b15 = Button(fr1, text="15", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2").place(
            x=500, y=450)
        b16 = Button(fr1, text="16", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2").place(
            x=750, y=5)
        b17 = Button(fr1, text="17", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2").place(
            x=750, y=120)
        b18= Button(fr1, text="18", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2").place(
            x=750, y=230)
        b19 = Button(fr1, text="19", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2").place(
            x=750, y=340)
        b20 = Button(fr1, text="20", padx=40, pady=20, command=lambda: self.myclick1(), height=5, width=20, bg="green2").place(
            x=750, y=450)
        ba = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20]
        for i in range(t1[0]):
            ba[i].config(bg="red")
            ba[i].config(command=lambda: self.myclick0())
    
            
       

    def vecy_fun(self):
        fr1 = Frame(self.root)
        fr1.place(x=270, y=120, width=980, height=550)
        fr2 = Frame(fr1, bg="white")
        fr2.place(x=100, y=0, width=500, height=550)
        global fname_txt
        global lname_txt
        global email_txt
        global questions
        global XYZ
        title1 = Label(fr2, text="ADD VEHICLE", font=("times new roman", 25, "bold"), bg="white").place(x=20, y=10)

        f_name = Label(fr2, text="First name", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=100)
        l_name = Label(fr2, text="Registration No", font=("helvetica", 15, "bold"), bg="white").place(x=240, y=100)

        fname_txt = Entry(fr2, font=("arial"))
        fname_txt.place(x=20, y=130, width=200)

        lname_txt = Entry(fr2, font=("arial"))
        lname_txt.place(x=240, y=130, width=200)

        email = Label(fr2, text="Email", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=180)

        email_txt = Entry(fr2, font=("arial"))
        email_txt.place(x=20, y=210, width=420)

        sec_question = Label(fr2, text="VEHICLE TYPE", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=260)
        XY1= Label(fr2, text="BLOCK_NUMBER", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=320)
        XYZ = Entry(fr2, font=("arial"))
        XYZ.place(x=20, y=350, width=420)

        questions = ttk.Combobox(fr2, font=("helvetica", 13), state='readonly', justify=CENTER)
        questions['values'] = ("Select", "2 WHEELER", "4 WHEELER")
        questions.place(x=120, y=300, width=200)
        questions.current(0)

        self.terms = IntVar()
        terms_and_con = Checkbutton(fr2, text="I Agree The Terms & Conditions", variable=self.terms, onvalue=1,
                                    offvalue=0, bg="white", font=("times new roman", 12)).place(x=20, y=380)
        self.signup = Button(fr2, text="ADD VEHICLE", font=("times new roman", 18, "bold"), bd=0, cursor="hand2",
                             bg="green2", fg="white", command=self.login_func)
        self.signup.place(x=50, y=430, width=250)

    def login_func(self):
        if fname_txt.get() == "" or lname_txt.get() == "" or email_txt.get() == "" or questions.get() == "Select":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.root)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!", "Please Agree with our Terms & Conditions", parent=self.root)

        else:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cur = connection.cursor()
            cur.execute("select email from student_register where email=%s", email_txt.get())
            row = cur.fetchone()

            # Check if th entered email id is already exists or not.
            if row != None:
                messagebox.showinfo("", "You are eligible to add vehicle", parent=self.root)
            
                sql = "insert into managehistory values(%s,%s,%s,%s,%s,%s);"
                sql1 = [fname_txt.get(), lname_txt.get(), email_txt.get(), questions.get(),XYZ.get(),200]
                cur.execute(sql, sql1)
                connection.commit()
                connection.close()
                messagebox.showinfo("Congratulations!", "Vehicle added Successful", parent=self.root)
                self.reset_fields()

    def macy_fun(self):
        labelFrame = Frame(self.root, bg='dark slate grey')
        labelFrame.place(x=270, y=120, height=550, width=980)
        y = 0.25
        Label(labelFrame, text="%-40s%-50s%-40s%-30s%-40s%-40s" % (
        'Name', 'Registration_No', 'E-mail', 'Gender', 'Block_No', 'Fare Price'), bg='dark slate grey',
              fg='white').place(relx=0.07, rely=0.1)
        Label(labelFrame,
              text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
              bg='dark slate grey', fg='white').place(relx=0.05, rely=0.2)
        connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
        cur = connection.cursor()
        sql = "select * from managehistory;"
        cur.execute(sql)
        connection.commit()
        for i in cur:
            Label(labelFrame, text="%-40s%-50s%-40s%-30s%-40s%-40s" % (i[0], i[1], i[2], i[3], i[4], i[5]),
                    bg='dark slate grey', fg='white').place(relx=0.07, rely=y)
            y += 0.1
        return

    def hist_fun(self):
        return
        
        
    def myclick0(self):
        messagebox.showinfo("","Slot is Occupied")
    def payment_fun():
        return
    def myclick1(self):
        messagebox.showinfo("","slot is vacant")
   


if __name__ == "__main__":
    root = Tk()
    obj = home(root)
    root.mainloop()
