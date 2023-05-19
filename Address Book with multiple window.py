## Adding Tkinter GUI to SQLite3 Database 

from tkinter import *
import sqlite3

root = Tk()
root.title("Adding GUI to SQLite3 Database")

def Add_data():
    ##Create new Window
    add_win = Toplevel()
    add_win.title("Add to Address Book")

    ####We comment out the below table cause we dont want to recreate the table everytime we run the program
    ####We will just use the table and add entries to it
    ####Create table for the database
    ##my_cursor.execute("""CREATE TABLE Addresses(
    ##        First_name text,
    ##        Last_name text,
    ##        Ph_num integer,
    ##        Address text,
    ##        City text,
    ##        State text,
    ##        Zipcode integer)
    ##    """)
    
    ##Create Clear function for textfields
    def Clear():
        #Clear the text boxes
        f_name.delete(0, END)
        l_name.delete(0, END)
        pho_no.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zipcode.delete(0, END)

    ##Create a Submit Function to Submit the details into database    
    def Submit():
        Clear()
        ##Create a database or connect to one
        conn = sqlite3.connect("address_book.db")
        ##Create Cursor
        myc = conn.cursor()
        ##Insert into Table
        myc.execute("INSERT INTO Addresses VALUES(:F_name, :L_name, :Phnum, :address, :city, :state, :zipcode)",
                    {
                        'F_name' : f_name.get(),
                        'L_name' : l_name.get(),
                        'Phnum' : pho_no.get(),
                        'address' : address.get(),
                        'city' : city.get(),
                        'state' : state.get(),
                        'zipcode' : zipcode.get()
                    }
        ) 
        ##Commit the changes to the databse
        conn.commit()
        ##Close the database
        conn.close()

    ##Creating Text boxes and labels
    f_name = Entry(add_win, width=30)
    f_name.grid(row=0,column=1, padx=20)
    f_nameLab = Label(add_win,text='First Name').grid(row=0,column=0)

    l_name = Entry(add_win, width=30)
    l_name.grid(row=1,column=1, padx=20)
    l_nameLab = Label(add_win,text='Last Name').grid(row=1,column=0)

    pho_no = Entry(add_win, width=30)
    pho_no.grid(row=2,column=1, padx=20)
    pho_noLab = Label(add_win,text='Phone Number').grid(row=2,column=0)

    address = Entry(add_win, width=30)
    address.grid(row=3,column=1, padx=20)
    addressLab = Label(add_win,text='Address').grid(row=3,column=0)

    city = Entry(add_win, width=30)
    city.grid(row=4,column=1, padx=20)
    cityLab = Label(add_win,text='City').grid(row=4,column=0)

    state = Entry(add_win, width=30)
    state.grid(row=5,column=1, padx=20)
    stateLab = Label(add_win,text='State').grid(row=5,column=0)

    zipcode = Entry(add_win, width=30)
    zipcode.grid(row=6,column=1, padx=20)
    zipcodeLab = Label(add_win,text='Zip Code').grid(row=6,column=0)

    ##Create a Submit button and a clear button
    submit_butt = Button(add_win, text="Clear",fg='red',bg='black',bd=5, command=Clear)
    submit_butt.grid(row=7,column=0,columnspan=1, pady=10,padx=10,ipadx=100)

    submit_butt = Button(add_win, text="Submit",fg='red',bg='black',bd=5, command=Submit)
    submit_butt.grid(row=7,column=1,columnspan=1, pady=10,padx=10,ipadx=100)

    ##Create a back button to go to main window
    back_butt = Button(add_win, text="Back to Main Menu",fg='red',bg='black',bd=10, command=add_win.destroy)
    back_butt.grid(row=8,column=0,columnspan=2, pady=10,padx=10,ipadx=100)
    
##---------------End of Add_data Function----------------------------------------------------------------

def View_data():
    view_win = Toplevel()
    view_win.title("Address Book")



    ##Buttons
    add_butt = Button(view_win, text="Input a Entry to the Address Book", fg='red',bg='black',bd=10,command=Add_data)
    add_butt.grid(row=0,column=0,columnspan=1, pady=10,padx=10,ipadx=100)

    ##Create a back button to go to main window
    back_butt = Button(view_win, text="Back to Main Menu",fg='red',bg='black',bd=10, command=view_win.destroy)
    back_butt.grid(row=0,column=1,columnspan=2, pady=10,padx=10,ipadx=100)
##----------------End of View_data Function---------------------------------------------------------------

add_butt = Button(root, text="Input a Entry to the Address Book", fg='red',bg='black',bd=10,command=Add_data)
add_butt.grid(row=0,column=0,columnspan=1, pady=10,padx=10,ipadx=100)

view_butt = Button(root, text="View Address Book",fg='red',bg='black', bd=10, command=View_data)
view_butt.grid(row=1,column=0,columnspan=1, pady=10,padx=10,ipadx=100)

exit_butt = Button(root, text="EXIT",fg='red',bg='black',bd=10,command=quit)
exit_butt.grid(row=2,column=0,pady=10,padx=10,ipadx=100)


root.mainloop()
