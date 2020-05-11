# FRONTEND FIRST

# A program that stores this book information:
# Title , Author 
# Year , ISBN 

# User can : 

# View all records 
# Search an entry 
# Add entry 
# Update an entry 
# Delete
# Close the program                              

from tkinter import *
import back

def get_selected_row(event):
    try:
        global selected_tuple             # to make it global so that it can work outside the function 
        index=lb.curselection()[0]
        selected_tuple=lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_comm():
    lb.delete(0,END)
    for row in back.view():
        lb.insert(END,row)

def search_comm():
    lb.delete(0 , END)
    for row in back.search(e1_v.get(),e2_v.get(),e3_v.get(),e4_v.get()):
        lb.insert(END,row)

def add_comm():
    back.insert(e1_v.get(),e2_v.get(),e3_v.get(),e4_v.get())
    lb.delete(0,END)
    lb.insert(END, (e1_v.get(),e2_v.get(),e3_v.get(),e4_v.get()))

def delete_comm():
    back.delete(selected_tuple[0])

def update_comm():
    back.update(selected_tuple[0],e1_v.get(),e2_v.get(),e3_v.get(),e4_v.get())
    # print(selected_tuple[0],e1_v.get(),e2_v.get(),e3_v.get(),e4_v.get())

window =Tk()

window.wm_title("BookStore")

b1= Button(window , text="View All" , width =12 , command = view_comm  )          # when we enter view() the view function executed when the python code runs but we need this function to run when the user press the view all button , for this write command = view instead of command = view()
b1.grid(row = 2 ,column =3 )

b2= Button(window , text="Search Entry", width =12 , command = search_comm )      # as search function has parameters we can't pass command as command = search_conn () 
b2.grid(row = 3 ,column =3 )

b3= Button(window , text="Add Entry", width =12 , command = add_comm)
b3.grid(row = 4 ,column =3 )

b4= Button(window , text="Update", width =12, command = update_comm)
b4.grid(row = 5 ,column =3 )

b5= Button(window , text="Delete", width =12 , command = delete_comm )
b5.grid(row = 6 ,column =3 )

b6= Button(window , text="Close", width =12 , command = window.destroy)
b6.grid(row = 7 ,column =3 )

e1_v =StringVar()
e1 = Entry(window , textvariable=e1_v)
e1.grid(row = 0, column =1)

e2_v =StringVar()
e2 = Entry(window , textvariable=e2_v)
e2.grid(row = 0, column =3)

e3_v =StringVar()
e3 = Entry(window , textvariable=e3_v)
e3.grid(row = 1, column =1)

e4_v =StringVar()
e4 = Entry(window , textvariable=e4_v)
e4.grid(row = 1, column =3)

l1= Label(window , text ="Title")
l1.grid(row = 0, column =0 )

l2= Label(window , text ="Author")
l2.grid(row = 0, column =2 )

l3= Label(window , text ="Year")
l3.grid(row = 1, column =0 )

l4= Label(window , text ="ISBN")
l4.grid(row =1 , column =2 )

s=Scrollbar(window )
s.grid(row = 2 , column =2 , rowspan = 6 )

lb=Listbox(window , height = 6 , width = 35 )
lb.grid(row =2  , column =0 , rowspan = 6 , columnspan = 2)

lb.configure(yscrollcommand=s.set)
s.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>' , get_selected_row)

window.mainloop()