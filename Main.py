from tkinter import *
from PIL import Image
from PIL import ImageTk
import pymysql
import tkinter.messagebox as mb




def about():
        import about

def add_students():
        import add_student

def issue_book():
        import book_issue2
def book_return():
        import book_return2

def statatics():
        import statatics

def add_book():
        import add_book



#-----------------------------Add Book-----------------------------------------

def add_new_book ():
        def add_book_close():
                add_ques=mb.askquestion("Close","Are You Sure ?")
                if add_ques=="yes":
                        add_book_root.destroy()

                
        def add_book_clear():
            book_id.delete(0,END)
            book_name.delete(0,END)
            book_isbn.delete(0,END)
            book_publisher.delete(0,END)
            book_edition.delete(0,END)
            book_price.delete(0,END)
            book_page.delete(0,END)
    

        def add_book_delete():
            id1=book_id.get()
            name=book_name.get()
            book_isbn1=book_isbn.get()
            publisher=book_publisher.get()
            edition=book_edition.get()
            price=book_price.get()
            page=book_page.get()
            con=pymysql.connect(host="localhost",user="root",password="123",db="library")
            cursor=con.cursor()
            cursor.execute("delete from add_book where Book_ID='"+book_id.get()+"'")
            ques=mb.askquestion("Delete","Are You Sure You Want To Delete Data")
            if ques=="yes":
                    cursor.execute("commit");
                    mb.showinfo("Deleted","Data Sucessfully Deleted")


        def add_book_insert():
                id1=book_id.get()
                name=book_name.get()
                book_isbn1=book_isbn.get()
                publisher=book_publisher.get()
                edition=book_edition.get()
                price=book_price.get()
                page=book_page.get()
                con=pymysql.connect(host="localhost",user="root",password="123",db="library")
                cursor=con.cursor()
                cursor.execute("insert into add_book values('"+id1 +"','"+ name+"','"+book_isbn1+"','"+publisher+"','"+edition +"','"+price+"','"+ page +"')")
                cursor.execute("commit");

                mb.showinfo("Inserted","Data Sucessfully Inserted")


        add_book_root=Toplevel()


        add_book_root.geometry("900x550")



        #Main Frame
        main_frame=Frame(add_book_root,bg="#d5d8de",height="550",width="900")
        main_frame.place(x=0,y=0)

        #Image
        image1= PhotoImage(file="add_book2.gif")
        label_for_image= Label(main_frame,image=image1)
        label_for_image.pack()







        #Entry And Labels
        #Left
        book_id=Entry(add_book_root,bd="5")
        book_id.place(x=425,y=185)

        book_name=Entry(add_book_root,bd="5")
        book_name.place(x=425,y=270)


        book_isbn=Entry(add_book_root,bd="5")
        book_isbn.place(x=425,y=350)


        book_publisher=Entry(add_book_root,bd="5")
        book_publisher.place(x=425,y=430)

        #Right
        book_edition=Entry(add_book_root,bd="5")
        book_edition.place(x=720,y=185)


        book_price=Entry(add_book_root,bd="5")
        book_price.place(x=720,y=270)


        book_page=Entry(add_book_root,bd="5")
        book_page.place(x=720,y=350)


        #Buttons
        #btn Frame
        btn_frame=Frame(main_frame,bg="#b0a897",height="100",width="350")
        btn_frame.place(x=450,y=470)

        insert=Button(btn_frame,text="Insert",bg="black",fg="white",bd="5",font="arial 12 bold",command=add_book_insert)
        insert.place(x=40,y=10)

        delete=Button(btn_frame,text="Delete",bg="black",fg="white",bd="5",font="arial 12 bold",command=add_book_delete)
        delete.place(x=135,y=10)

        close=Button(btn_frame,text="Close",bg="black",fg="white",bd="5",font="arial 12 bold")
        close.place(x=250,y=10)
        





#-----------------------------Main Window-----------------------------------------
root=Toplevel()

root.iconbitmap(r'book.ico')



root.geometry("850x650")
root.title("Library Management System")
root.minsize(width="850",height="650")
root.maxsize(width="850",height="650")


top_frame=Frame(root,bg="black",height="110",width="850")
top_frame.place(x=0,y=0)
libheading=Label(top_frame,text="Library Management System",font="arial 30 bold",fg="white",bg="black")
libheading.place(x=170,y=30)





#Frame 1

frame1=Frame(root,bg="#f7ece6",height="200",width="800")
frame1.place(x=0,y=100)

#Image
image1= PhotoImage(file="background.gif")
label_for_image= Label(frame1, image=image1)
label_for_image.pack()




#Imgs
add_book_img=PhotoImage(file="add6.png")
sta_img=PhotoImage(file="sta.png")
add_stu_img=PhotoImage(file="add_stu3.png")
issue_img=PhotoImage(file="issue.png")
return_img=PhotoImage(file="return.png")
info_img=PhotoImage(file="info_img.png")




#Frame1 Buttons
add_book_btn=Button(frame1,bg="black",height="200",width="220",image=add_book_img,command=add_book)
add_book_btn.place(x=20,y=5)

stastics_btn=Button(frame1,bg="black",height="200",width="220",image=sta_img,command=statatics)
stastics_btn.place(x=280,y=5)


add_student_btn=Button(frame1,bg="black",height="200",width="220",image=add_stu_img,command=add_students)
add_student_btn.place(x=560,y=5)



issue_book_btn=Button(frame1,bg="black",height="200",width="220",image=issue_img,command=issue_book)
issue_book_btn.place(x=20,y=250)

return_book=Button(frame1,bg="black",height="200",width="220",image=return_img,command=book_return)
return_book.place(x=280,y=250)


about_lib=Button(frame1,bg="black",height="200",width="220",image=info_img,command=about)
about_lib.place(x=560,y=250)


root.mainloop()
