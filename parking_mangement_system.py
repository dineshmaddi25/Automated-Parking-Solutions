from msilib.schema import ComboBox
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from HOME_PAGE_PK import *
import credentials as cr
import pymysql
from tkinter import ttk
import subprocess
from signup_page import SignUp



 
        
        

class login(Frame):
  
        
    def __init__(self, root):
        self.root = root
        self.root.title("PARKING MANGEMENT SYsTEM")
        self.root.geometry("1280x800+0+0")
        self.root.resizable(True, True)
        self.lt = Label(self.root, text="Parking Management System", bg="black", fg="white", bd=20,
                        font=("times new roman", 30, "bold"), padx=2, pady=6)
        
        self.lt.pack(side=TOP, fill=X)
        self.fr = Frame(self.root,  bg="black")
        self.fr.place(x=0, y=100, width=1300, height=600)
        self.bg = ImageTk.PhotoImage(file="E:/GUI USING TKINTER/image/home.jpg")
        self.bg_image = Label(self.fr, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)


        

        frame_login = Frame(self.fr, bg="white")

        frame_login.place(x=400, y=150, height=300, width=400)
        self.b1 = Button(frame_login, height=5, width=14, bg="black", fg="white", bd=0, text="Login",
                         font=("times new roman", 13, "bold"), command=lambda: self.Login())
        self.b2 = Button(frame_login, height=5, width=14, bg="black", fg="white", bd=0, text="New User",
                         font=("times new roman", 13, "bold"), command=lambda:self.redirect_window())
        self.b3 = Button(frame_login, height=5, width=14, bg="black", fg="white", bd=0, text="MAIN MENU",
                         font=("times new roman", 13, "bold"), command=lambda: self.Login())
        self.b1.place(x=10, y=10)
        self.b2.place(x=230, y=10)
        self.b3.place(x=130, y=170)
    def home1(self):
           
            
    
        self.root = root
        self.root.title("PARKING MANGEMENT SYsTEM")
        self.root.geometry("1280x800+0+0")
        self.root.resizable(False, False)
        self.lt = Label(self.root, text="Parking Management System", bg="black", fg="white", bd=20,
                        font=("times new roman", 30, "bold"), padx=2, pady=6)
        
        self.lt.pack(side=TOP, fill=X)
        self.fr = Frame(self.root,  bg="black")
        self.fr.place(x=0, y=100, width=1300, height=600)
        self.bg = ImageTk.PhotoImage(file="E:/GUI USING TKINTER/image/home.jpg")
        self.bg_image = Label(self.fr, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)


        

        frame_login = Frame(self.fr, bg="white")

        frame_login.place(x=400, y=150, height=300, width=400)
        self.b1 = Button(frame_login, height=5, width=14, bg="black", fg="white", bd=0, text="Login",
                         font=("times new roman", 13, "bold"), command=lambda: self.Login())
        self.b2 = Button(frame_login, height=5, width=14, bg="black", fg="white", bd=0, text="New User",
                         font=("times new roman", 13, "bold"), command=lambda:self.redirect_window())
        self.b3 = Button(frame_login, height=5, width=14, bg="black", fg="white", bd=0, text="MAIN MENU",
                         font=("times new roman", 13, "bold"), command=lambda: self.Login())
        self.b1.place(x=10, y=10)
        self.b2.place(x=230, y=10)
        self.b3.place(x=130, y=170)

    def Login(self):
        self.fr = Frame(self.root, bd=10, padx=10, bg="black")
        self.fr.place(x=0, y=100, width=1300, height=600)

        self.bg = ImageTk.PhotoImage(file="E:/GUI USING TKINTER/image/website_keyvisual_parking.jpg")
        self.bg_image = Label(self.fr, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)
        # login frame
        fl = Frame(self.fr, bg="white")
        fl.place(x=400, y=100, height=400, width=390)
        title = Label(fl, text="Login Here", font=("Impact", 30, "bold"), bg="white").place(x=40, y=10)
        lbl_username = Label(fl, text="Username", font=("goud old style", 15, "bold"), bg="white", fg="gray")
        self.txt_user = Entry(fl, font=("times new roman", 15), bg="lightgray")
        lbl_username.place(x=40, y=70)
        self.txt_user.place(x=40, y=100, width=300, height=30)
        lbl_pass = Label(fl, text="password", font=("goud old style", 15, "bold"), bg="white", fg="gray")
        lbl_pass.place(x=40, y=140)
        self.txt_pass = Entry(fl, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=40, y=170, width=300, height=30)
        forget = Button(fl, text="forgot your password?", bg="white", bd=0, fg="black",command=self.forgot_func,
                        font=("times new roman", 12)).place(x=40, y=220)
        login_btn = Button(self.root, text="Login", bg="black", fg="white", font=("times new roman", 20),
                           command=self.login_func).place(x=460, y=480, width=140, height=40)
        create_btn = Button(self.root, text="Create New Account",bg="black", fg="white", font=("times new roman", 15),
                           command=self.redirect_window).place(x=620, y=480, width=180, height=40)
        back_btn = Button(self.root, text="Back to main page",bg="black", fg="white", font=("times new roman", 15),
                           command=self.home1).place(x=520, y=560, width=180, height=40)
   
    def login_func(self):
        if self.txt_user.get() == "" and self.txt_pass.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.root)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and password=%s",
                            (self.txt_user.get(), self.txt_pass.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "Invalid USERNAME & PASSWORD", parent=self.root)
                    
                else:
                    messagebox.showinfo("Success","Wellcome to PARKING MANAGEMENT SYSTEM",parent=self.root)
                    # Clear all the entries
                    self.redirect_window1()
                    self.reset_fields()
                    
                    connection.close()

           

                

            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.root)
 

    
    def forgot_func(self):
        if self.txt_user.get() == "":
            messagebox.showerror("Error!", "Please enter your User Id", parent=self.root)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s", self.txt_user.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "userid doesn't exists")
                else:
                    connection.close()

                    # =========================SECOND WINDOW===============================
                    # ------------Toplevel:create a window top of another window-----------
                    # ------------focus_force:Helps to to focus on the current window------
                    # -----Grab:Helps to grab the current window until user ungrab it------

                    self.root = Toplevel()
                    self.root.title("Forget Password?")
                    self.root.geometry("400x440+450+200")
                    self.root.config(bg="white")
                    self.root.focus_force()
                    self.root.grab_set()

                    title3 = Label(self.root, text="Change your password", font=("times new roman", 20, "bold"),
                                   bg="white").place(x=10, y=10)

                    title4 = Label(self.root, text="It's quick and easy", font=("times new roman", 12),
                                   bg="white").place(x=10, y=45)

                    title5 = Label(self.root, text="Select your question", font=("times new roman", 15, "bold"),
                                   bg="white").place(x=10, y=85)

                    self.sec_ques = ttk.Combobox(self.root, font=("times new roman", 13), state='readonly',
                                                 justify=CENTER)
                    self.sec_ques['values'] = (
                    "Select", "What's your pet name?", "Your first teacher name", "Your birthplace",
                    "Your favorite movie")
                    self.sec_ques.place(x=10, y=120, width=270)
                    self.sec_ques.current(0)

                    title6 = Label(self.root, text="Answer", font=("times new roman", 15, "bold"), bg="white").place(
                        x=10, y=160)

                    self.ans = Entry(self.root, font=("arial"))
                    self.ans.place(x=10, y=195, width=270)

                    title7 = Label(self.root, text="New Password", font=("times new roman", 15, "bold"),
                                   bg="white").place(x=10, y=235)

                    self.new_pass = Entry(self.root, font=("arial"))
                    self.new_pass.place(x=10, y=270, width=270)

                    self.create_button = Button(self.root, text="Submit", command=self.change_pass,
                                                font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2",
                                                fg="white").place(x=95, y=340, width=200)
                    # =========================================================================

            except Exception as e:
                messagebox.showerror("Error", f"{e}")

    def change_pass(self):
        if self.txt_user.get() == "" or self.sec_ques.get() == "Select" or self.new_pass.get() == "":
            messagebox.showerror("Error!", "Please fill the all entry field correctly")
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and question=%s and answer=%s",
                            (self.txt_user.get(), self.sec_ques.get(), self.ans.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "Please fill the all entry field correctly")
                else:
                    try:
                        cur.execute("update student_register set password=%s where email=%s",
                                    (self.new_pass.get(), self.txt_user.get()))
                        connection.commit()

                        messagebox.showinfo("Successful", "Password has changed successfully")
                        connection.close()
                        self.reset_fields()
                        self.root.destroy()

                    except Exception as er:
                        messagebox.showerror("Error!", f"{er}")

            except Exception as er:
                messagebox.showerror("Error!", f"{er}")

    def redirect_window(self):
         self.root.destroy()
         # Importing the signup window.
        # The page must be in the same directory
         root = Tk()
         obj = SignUp(root)
         root.mainloop()
    def redirect_window1(self):
         self.root.destroy()
         # Importing the signup window.
        # The page must be in the same directory
         root = Tk()
         obj = home(root)
         root.mainloop()
         


    
            
      
   
        
    def reset_fields(self):
        self.txt_user.delete(0, END)
        self.txt_pass.delete(0, END)    
if __name__ == "__main__":   
     root = Tk()
     obj = login(root)
     root.mainloop()
