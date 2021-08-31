from tkinter import *
root=Tk()
import csv
root.geometry("944x855")

# Making frame

f1=Frame(root,bg="black",borderwidth=6,relief="sunken")
f1.pack(fill="both")

# Making the funtion for output
def getvals():
	print("program works!!!!")
	with open("records.csv","w",newline="") as f:
		pen=csv.writer(f)
		rec=[f"{Student_namevalue.get(),Father_namevalue.get(),Mother_namevalue.get(),Classvalue.get(),Contect_numbervalue.get(),E_mail_idvalue.get(),Current_addressvalue.get()}"]
		pen.writerow(rec)
	f.close()


# Making label for user name
Label(f1,text="Addmision_no",bg="black",fg="white",borderwidth=6,relief="sunken",pady=16).grid(row=1, column=3)

# Making label for password
Label(f1,text="Student_name",bg="black",fg="white",borderwidth=6,relief="sunken",pady=16).grid(row=2, column=3)# Making label for E-mail  id 
Label(f1,text="Father's_name",bg="black",fg="white",borderwidth=6,relief="sunken",pady=16).grid(row=3, column=3)

Label(f1,text="Mother's_name",bg="black",fg="white",borderwidth=6,relief="sunken",pady=16).grid(row=4, column=3)

Label(f1,text="Class",bg="black",fg="white",borderwidth=6,relief="sunken",pady=16).grid(row=5, column=3)

Label(f1,text="Contect_number",bg="black",fg="white",borderwidth=6,relief="sunken",pady=16).grid(row=6, column=3)

Label(f1,text="E-mail_id",bg="black",fg="white",borderwidth=6,relief="sunken",pady=16).grid(row=7, column=3)

Label(f1,text="Current_address",bg="black",fg="white",borderwidth=6,relief="sunken",pady=16).grid(row=8, column=3)
# Making values
Addmision_novalue=StringVar()
Student_namevalue=StringVar()
Father_namevalue=StringVar()
Mother_namevalue=StringVar()
Classvalue=StringVar()
Contect_numbervalue=StringVar()
E_mail_idvalue=StringVar()
Current_addressvalue=StringVar()

# Making & pack enters
Addmision_no_entry=Entry(f1,textvariable=Addmision_novalue)
Addmision_no_entry.grid(row=1, column=6)


Student_name_entry=Entry(f1,textvariable=Student_namevalue)
Student_name_entry.grid(row=2, column=6)

Father_name_entry=Entry(f1,textvariable=Father_namevalue)
Father_name_entry.grid(row=3, column=6)

Mother_name_entry=Entry(f1,textvariable=Mother_namevalue)
Mother_name_entry.grid(row=4, column=6)

Class_entry=Entry(f1,textvariable=Classvalue)
Class_entry.grid(row=5, column=6)

Contect_number_entry=Entry(f1,textvariable=Contect_numbervalue)
Contect_number_entry.grid(row=6, column=6)

E_mail_id_entry=Entry(f1,textvariable=E_mail_idvalue)
E_mail_id_entry.grid(row=7, column=6)

Current_address_entry=Entry(f1,textvariable=Current_addressvalue)
Current_address_entry.grid(row=8, column=6)

# Making buttons
Button(f1,text="Submit to Abhishek", fg="red",borderwidth=8,relief="sunken",command=getvals).grid(row=9, column=6)

root.mainloop()
