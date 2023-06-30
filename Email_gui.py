from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import smtplib
from tkinter.scrolledtext import ScrolledText


root = tk.Tk()
root.title("Mail Sender Application")
root.iconbitmap('mail-icon.ico')
root.geometry('750x450')
root.resizable(False,False)

img = ImageTk.PhotoImage(Image.open('back-1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('back-2.jpg'))

back1 = Label(root,image=img, borderwidth=0)
back1.pack()

def Login():
    e = email.get()
    p = password.get()
    if '@gmail.com' not in e or e == "":
        messagebox.showerror('Login Error',"Please Enter the Valid Gmail Id")
    elif p == "":
        messagebox.showerror('Login Error',"Incorrect Password")
    else:
        try:
            # s = smtplib.SMTP('smtp.gmail.com',587)
            s = smtplib.SMTP_SSL('smtp.gmail.com',465)
            # s.starttls()
            s.ehlo()
            s.login(e,p) #attempt to login
            messagebox.showinfo("Login Success","You have Logged in to Gmail Successfully")

            root1 = tk.Toplevel()
            root1.geometry('750x450')
            root1.title('Mail Sender Application')
            root1.iconbitmap('mail-icon.ico')
            root1.resizable(False,False)
            root.withdraw()
            
            back = Label(root1,image=img)
            back.pack()

            def Logout():
                    s.quit()
                    root.destroy()

            log_frame1 = Frame(root1,bg='wheat',bd='5',relief=RIDGE)
            log_frame1.place(x=80,y=80,width=300,height=320)

            h1 = Label(root1,text=' Gmail Sender ',bg='light blue',fg='black',font=('vardana',14,'bold'))
            h1.place(x=140,y=35)

            r = Label(log_frame1,text="Recipent Gmail Address",bg='wheat',font=('verdana',10,'bold'))
            r.place(x=10,y=10)
            recipetent = Entry(log_frame1,width=40,relief=GROOVE,borderwidth=3)
            recipetent.place(x=10,y=35)

            st = Label(log_frame1,text="Subject",bg='wheat',font=('verdana',10,'bold'))
            st.place(x=10,y=70)
            subject = Entry(log_frame1,width=40,relief=GROOVE,borderwidth=3)
            subject.place(x=10,y=95)

            m = Label(log_frame1,text="Compose",bg='wheat',font=('verdana',10,'bold'))
            m.place(x=10,y=125)
            message = ScrolledText(log_frame1,width=30,height=6,relief=RIDGE,borderwidth=3)
            message.place(x=5,y=150)

            def Send():
                    r = recipetent.get()
                    st = subject.get()
                    m = message.get('1.0',END)
                    if r == "":
                            messagebox.showerror('Sending Mail error',"Please Write the Valid Email")
                    elif m == "":
                            messagebox.showerror('Sending Mail error',"Message shouldn't be Empty")
                    else:
                         s.sendmail(e,r,f'Subject :{st}\n\n {m}')
                         messagebox.showinfo("Success","Your Message has been send successfully")

            btn1 = Button(root1,text="Log out",bg='green',font=('verdana',10,'bold'),width=8,height=1,cursor="hand2",borderwidth=1,relief=RIDGE,command=Logout)
            btn1.place(x=650,y=20)

            btn2 = Button(log_frame1,text="Send",bg='green',font=('verdana',10,'bold'),width=8,height=1,cursor="hand2",borderwidth=1,relief=RIDGE,command=Send)
            btn2.place(x=100,y=270)
        except:
            messagebox.showinfo("Login Error","Failed to Login, Check Gmail ID and Password")
            # root1.mainloop()
            # root.withdraw()

log_frame = Frame(root,bg='wheat',bd='5',relief=RIDGE)
log_frame.place(x=80,y=80,width=250,height=300)

h1 = Label(root,text=' Gmail Login ',bg='light blue',fg='black',font=('vardana',14,'bold'))
h1.place(x=140,y=35)

e = Label(log_frame,text="Gmail Address",bg='wheat',font=('verdana',10,'bold'))
e.place(x=10,y=25)
email = Entry(log_frame,width=30,relief=GROOVE,borderwidth=3)
email.place(x=10,y=50)

p = Label(log_frame,text="Password",bg='wheat',font=('verdana',10,'bold'))
p.place(x=10,y=95)
password = Entry(log_frame,show='*',width=30,relief=GROOVE,borderwidth=3)
password.place(x=10,y=120)

btn = Button(log_frame,text="Submit",bg='green',font=('verdana',10,'bold'),width=8,height=1,cursor="hand2",borderwidth=1,relief=RIDGE, command=Login)
btn.place(x=60,y=180)

root.mainloop()         