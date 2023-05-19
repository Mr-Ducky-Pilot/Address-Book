## Address Book Application using Tkinter and SQLite3

from tkinter import *
from tkinter import messagebox
import sqlite3

##Main window
root = Tk()
root.title("Adding GUI to SQLite3 Database")

##Create a database or connect to one
##conn = sqlite3.connect("address_book.db")

##Create Cursor, it is used to execute commands and do stuff with the database
##my_cursor = conn.cursor()

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

##Commit is used to implement the changes to the databse
##conn.commit()

##Close the database, not completely necessary but a good pratice to close it manually to prevent any incidents
##conn.close()

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
##-------------------------------------------------------------------------------------------------------------------------------------
    
##Create a Submit Function to Submit the details into database    
def Submit():
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

    ##Call the clear function to clear the text boxes
    Clear()

##Validation Function:------------------------------------------------------------
def Validation():
    ##initial valid is set to yes every time submit button is clicked
    vaild='yes'
    ##Perfrom First Name validation
    name = f_name.get()
    msg = ''
    ## if statements to check if name has any numbers or is too short or long
    if len(name) == 0:
        msg = 'name can\'t be empty'
    else:
        try:
            if any(ch.isdigit() for ch in name):
                msg = 'Name can\'t have numbers'
                valid='no'
            elif len(name) <= 2:
                msg = 'name is too short.'
                valid='no'
            elif len(name) > 30:
                msg = 'name is too long.'
                valid='no'
            else:
                valid='yes'
        except Exception as ep:
            messagebox.showerror('error', ep)
            valid='no'
    if valid !='yes':
        ##Print error message window if name fails above condition
        messagebox.showinfo('message', msg)

    ##Phone Number Validation--------------------------------------------------------------------------------------
    if valid=='yes':
        msgg = ''
        num = pho_no.get()
        if len(num)==0:
            msgg='Phone Num can\'t be empty'
        else:
            try:
                if int(len(num)) < 10:
                    msgg='Phone Num cannot be less than 10 digits'
                    valid='no'
                elif int(len(num)) >10:
                    msgg='Phone Num cannot be more than 10 digits'
                    valid='no'
                else:
                    valid='yes'
            except:
                msgg='Phone Number cannot have characters'
                valid='no'
        if valid !='yes':
            messagebox.showinfo('info', msgg)

    ## If both validation are cleared then call the submit function and insert the data into the database
    if valid=='yes':
        Submit()

##-------------------------------------------------------------------------------------------------------------------------------------
    
##Query function to show data from the database
def query():
    ##Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    ##Create Cursor
    myc = conn.cursor()

    ##Query the database
    myc.execute("SELECT *,oid FROM Addresses")
    records = myc.fetchall()                                    ##3hr:50min differnent types of fetch 
    ##print(records) 
    print_rec = 'Id_No |    Name    |     Last_Name  |    Phone_Num    |    Address    |    City    |    State    |    ZipCode    |\n'
    for rec in records:
        print_rec += str(rec[7])+"  |  "+str(rec[0]) +"  |  "+str(rec[1]) +"  |  "+str(rec[2]) +"  |  "+str(rec[3]) +"  |  "+str(rec[4]) +"  |  "+str(rec[5]) +"  |  "+str(rec[6]) +"  |\n" 

    query_lab = Label(root,text=print_rec)
    query_lab.grid(row=10,column=0,columnspan=2)
    
    ##Commit the changes to the databse
    conn.commit()
    ##Close the database
    conn.close()

    ##Creating a box to select which id to delete from the database
    global del_id
    del_id= Entry(root, width=30)
    del_id.grid(row=11,column=1, padx=20)
    del_idLab = Label(root,text='Enter Id to Delete').grid(row=11,column=0)
    
    ##Create a button for Delete function
    delete_butt = Button(root, text="Delete from Database ",fg='red',bg='black',command=query_del)
    delete_butt.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
##-------------------------------------------------------------------------------------------------------------------------------------

##Function to Delete a query/data
def query_del():
    ##Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    ##Create Cursor
    myc = conn.cursor()

    ##Delete a record from database
    myc.execute("DELETE FROM Addresses WHERE oid="+del_id.get())
    
    ##Commit the changes to the databse
    conn.commit()
    ##Close the database
    conn.close()
##-------------------------------------------------------------------------------------------------------------------------------------  
##Function to edit data in the database
def edit_query():
    edit_win = Toplevel()
    edit_win.title("Update Query")

    ##Create a entry field to select if for update
    edit_id= Entry(edit_win, width=30)
    edit_id.grid(row=0,column=1, padx=20)
    edit_idLab = Label(edit_win,text='Enter Id to Update').grid(row=0,column=0)

    def edit():
        ##Create a database or connect to one
        conn = sqlite3.connect("address_book.db")
        ##Create Cursor
        myc = conn.cursor()
        ##Getting the data from Database
        myc.execute("SELECT *  FROM Addresses WHERE oid=" + edit_id.get())
        records = myc.fetchall()

        info_label = Label(edit_win, text='Please Update the Info Below and click UPDATE button')
        info_label.grid(row=2,column=0,columnspan=2, pady=(10,0))

        ##Entry Text Boxes and Labels for the window
        f_nameEdit = Entry(edit_win, width=30)
        f_nameEdit.grid(row=3,column=1, padx=20,pady=(10,0))
        f_nameEditLab = Label(edit_win,text='First Name').grid(row=3,column=0,pady=(10,0))

        l_nameEdit = Entry(edit_win, width=30)
        l_nameEdit.grid(row=4,column=1, padx=20)
        l_nameEditLab = Label(edit_win,text='Last Name').grid(row=4,column=0)

        pho_noEdit = Entry(edit_win, width=30)
        pho_noEdit.grid(row=5,column=1, padx=20)
        pho_noEditLab = Label(edit_win,text='Phone Number').grid(row=5,column=0)

        addressEdit = Entry(edit_win, width=30)
        addressEdit.grid(row=6,column=1, padx=20)
        addressEditLab = Label(edit_win,text='Address').grid(row=6,column=0)

        cityEdit = Entry(edit_win, width=30)
        cityEdit.grid(row=7,column=1, padx=20)
        cityEditLab = Label(edit_win,text='City').grid(row=7,column=0)

        stateEdit = Entry(edit_win, width=30)
        stateEdit.grid(row=8,column=1, padx=20)
        stateEditLab = Label(edit_win,text='State').grid(row=8,column=0)

        zipcodeEdit = Entry(edit_win, width=30)
        zipcodeEdit.grid(row=9,column=1, padx=20)
        zipcodeEditLab = Label(edit_win,text='Zip Code').grid(row=9,column=0)

         ##Loop through records
        for rec in records:
            f_nameEdit.insert(0,rec[0])
            l_nameEdit.insert(0,rec[1])
            pho_noEdit.insert(0,rec[2])
            addressEdit.insert(0,rec[3])
            cityEdit.insert(0,rec[4])
            stateEdit.insert(0,rec[5])
            zipcodeEdit.insert(0,rec[6])

        def update():
            ##Create a database or connect to one
            conn = sqlite3.connect("address_book.db")
            ##Create Cursor
            myc = conn.cursor()
            myc.execute("""UPDATE Addresses SET
                First_name = :first,
                Last_name = :last,
                Ph_num = :ph_no,
                Address = :address,
                City = :city,
                State = :state,
                Zipcode = :zipcode

                WHERE oid = :oid""",
                {'first' : f_nameEdit.get(),
                 'last' : l_nameEdit.get(),
                 'ph_no' : pho_noEdit.get(),
                 'address' : addressEdit.get(),
                 'city' : cityEdit.get(),
                 'state' : stateEdit.get(),
                 'zipcode' : zipcodeEdit.get(),

                 'oid' : edit_id.get()
                })
            ##Commit the changes to the databse
            conn.commit()
            ##Close the database
            conn.close()
            ##Clear the text fields
            f_nameEdit.delete(0, END)
            l_nameEdit.delete(0, END)
            pho_noEdit.delete(0, END)
            addressEdit.delete(0, END)
            cityEdit.delete(0, END)
            stateEdit.delete(0, END)
            zipcodeEdit.delete(0, END)
    
        ##Commit the changes to the databse
        conn.commit()
        ##Close the database
        conn.close()

        ##Create a Edit Button to edit a record in the database
        update_butt = Button(edit_win, text="Edit Records",fg='red',bg='black',command=update)
        update_butt.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

    ##Create a get record button
    info_butt = Button(edit_win, text="Get Record",fg='red',bg='black',command=edit)
    info_butt.grid(row=1,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

    ##Button to go back to main window
    main_butt = Button(edit_win, text="Go Back to Main Window?",fg='red',bg='black',command=edit_win.destroy)
    main_butt.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=100)




##-------------------------------------------------------------------------------------------------------------------------------------


##Creating Text boxes and labels
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1, padx=20,pady=(10,0))
f_nameLab = Label(root,text='First Name').grid(row=0,column=0,pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1,column=1, padx=20)
l_nameLab = Label(root,text='Last Name').grid(row=1,column=0)

pho_no = Entry(root, width=30)
pho_no.grid(row=2,column=1, padx=20)
pho_noLab = Label(root,text='Phone Number').grid(row=2,column=0)

address = Entry(root, width=30)
address.grid(row=3,column=1, padx=20)
addressLab = Label(root,text='Address').grid(row=3,column=0)

city = Entry(root, width=30)
city.grid(row=4,column=1, padx=20)
cityLab = Label(root,text='City').grid(row=4,column=0)

state = Entry(root, width=30)
state.grid(row=5,column=1, padx=20)
stateLab = Label(root,text='State').grid(row=5,column=0)

zipcode = Entry(root, width=30)
zipcode.grid(row=6,column=1, padx=20)
zipcodeLab = Label(root,text='Zip Code').grid(row=6,column=0)

##Create a Clear button
clr_butt = Button(root, text="Clear",fg='red',bg='black', command=Clear)
clr_butt.grid(row=7,column=0,columnspan=1, pady=10,padx=10,ipadx=100)

##Create a Submit button
submit_butt = Button(root, text="Submit",fg='red',bg='black', command=Validation)
submit_butt.grid(row=7,column=1,columnspan=1, pady=10,padx=10,ipadx=100)

##Create a View Button to see data in the database
query_butt = Button(root, text="View Records",fg='red',bg='black',command=query)
query_butt.grid(row=8,column=0,columnspan=1,pady=10,padx=10,ipadx=100)

##Create a Edit Button to edit a record in the database
edit_butt = Button(root, text="Edit Records",fg='red',bg='black',command=edit_query)
edit_butt.grid(row=8,column=1,columnspan=1,pady=10,padx=10,ipadx=100)

##Create a quit button
exit_butt = Button(root, text="EXIT",fg='red',bg='black',command=quit)
exit_butt.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

root.mainloop()
