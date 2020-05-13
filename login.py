from tkinter import *
import tkinter.messagebox as mb



def login():
    user=user_id.get()
    pass1=password.get()
    if user=="admin" and pass1=="admin":
        root_login.destroy()
        import Main

    elif user!="admin" or pass1 !="admin":
        mb.showinfo("Bad Login","Incorrect Username or password")

    else:
        print("")
        

root_login=Tk()

root_login.geometry("900x500")


login_frame=Frame(root_login,bg="red",height="500",width="900")
login_frame.place(x=0,y=0)

#Image
image1= PhotoImage(file="login_bg.gif")
label_for_image= Label(login_frame, image=image1)
label_for_image.pack()

#Label And Entry
user_id=Entry(root_login,bd="5")
user_id.place(x=650,y=230)


password=Entry(root_login,bd="5",show="*")
password.place(x=650,y=310)

#Label And Entry



b1=Button(root_login,text="Login",bg="black",fg="white",bd="5",font="arial 12 bold",command=login)
b1.place(x=690,y=360)

root_login.mainloop()
