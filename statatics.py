from tkinter import *
import pymysql


def return_book_data():
        con=pymysql.connect(host="localhost",user="root",password="123",db="library")
        cursor=con.cursor()
        cursor.execute("select * from book_return2 ")
        row=cursor.fetchall()
        list2.delete(0,list2.size())

        for row in row:
            insertData=row[0]+'        '+row[1]+'      '+row[2]+'      '+row[3]+'      ' +row[4]+'     ' +(str(row[5]))+'  ''     ' +(str(row[6]))+'   '
            list2.insert(list2.size()+1,insertData)
            


def issue_book_data():
        con=pymysql.connect(host="localhost",user="root",password="123",db="library")
        cursor=con.cursor()
        cursor.execute("select * from book_issue ")
        row=cursor.fetchall()
        list1.delete(0,list1.size())

        for row in row:
            insertData2=row[0]+'        '+row[1]+'      '+row[2]+'      '+row[3]+'      ' +row[4]+'     ' +(str(row[5]))+'  ''     ' +(str(row[6]))+'   '
            list1.insert(list1.size()+1,insertData2)
            
statatics_root=Toplevel()
statatics_root.geometry("750x650")
statatics_root.minsize(width="750",height="650")
statatics_root.maxsize(width="850",height="650")



statatics_root.title("Statatic")



#Image
image1= PhotoImage(file="background.gif")
label_for_image= Label(statatics_root, image=image1)
label_for_image.pack()


sta_heading_frame=Frame(statatics_root,bg="black",height="110",width="850")
sta_heading_frame.place(x=0,y=0)
sta_heading=Label(sta_heading_frame,text="Statatics",font="arial 30 bold",fg="white",bg="black")
sta_heading.place(x=300,y=30)

#Issue Frame
issue_book_frame=Frame(statatics_root,bg="#f7ece6",height="200",width="500")
issue_book_frame.place(x=150,y=170)

issue_heading=Label(statatics_root,text="Books Issue",font="arial 20 bold",fg="white",bg="black")
issue_heading.place(x=150,y=120)

#List Box Issue
list1=Listbox(issue_book_frame,height="200",width="800")
list1.place(x=0,y=0)
issue_book_data()



#Return Frame
return_book_frame=Frame(statatics_root,bg="#f7ece6",height="200",width="500")
return_book_frame.place(x=150,y=430)

return_heading=Label(statatics_root,text="Books Return",font="arial 20 bold",fg="white",bg="black")
return_heading.place(x=150,y=385)

list2=Listbox(return_book_frame,height="200",width="800")
list2.place(x=0,y=0)
return_book_data()


statatics_root.mainloop()
