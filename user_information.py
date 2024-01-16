import tkinter as tk
from tkinter import ttk, messagebox
#import mysql.connector 

class Page1(tk.Frame):
    def __init__(self, root, show_main_menu):
        super().__init__(root, width=400, height=300)
        label = tk.Label(self, text="Page 1", font=('Helvetica', 18))
        label.pack(pady=20)

        back_button = tk.Button(self, text="Back to Main Menu", command=show_main_menu)
        back_button.pack(pady=10)

#mydb = mysql.connector.connect(
    #host ="localhost",
    #user ="root",
    #password = "", 
    #database="student_information")

#mycursor=mydb.cursor()

def insert_data():
    try:
        label_name = name_entry.get()
        label_ic_number = ic_number_entry.get()
        label_address = address_entry.get()
        label_gender= gender_entry.get()
        label_age = age_entry.get()
        
        print("Name:", label_name)
        print("ic number:",label_ic_number )
        print("address:",label_address)
        print(" gender", label_gender)
        print("age:", label_age) 
        
        #sql=("INSERT INTO student information (NAME,IC NUMBER,ADDRESS,GENDER,AGE,PLACE ) VALUES(%s,%s,%s,%s,%s,%s)")
        #val=(label_name, label_ic_number, label_address, label_gender, label_age, label_place,)
    
        #mycursor.execute(sql,val)
        #mydb.commit()

        messagebox.showinfo("Success", "Student information inserted successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def delete_data():
    try:
        # Uncomment the following lines when you have a working database connection
        # selected_id = # Get the selected ID from the user interface or another source
        # sql = "DELETE FROM student_information WHERE ID = %s"
        # val = (selected_id,)
        # mycursor.execute(sql, val)
        # mydb.commit()

        messagebox.showinfo("Success", "Student information deleted successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def update_data():
    try:
        # Uncomment the following lines when you have a working database connection
        #selected_id = # Get the selected ID from the user interface or another source
        #new_name = # Get the updated name from the user interface or another source
        #new_ic_number = # Get the updated IC number from the user interface or another source

        #sql = "UPDATE student_information SET NAME = %s, IC_NUMBER = %s WHERE ID = %s"
        #val = (new_name, new_ic_number, selected_id)
        # mycursor.execute(sql, val)
        # mydb.commit()

        messagebox.showinfo("Success", "Student information updated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
# Tkinter GUI
root = tk.Tk()
root.title("student_information")
root.geometry("500x600")
root.configure(bg="#27408B")

label = tk.Label(root, text="STUDENT INFORMATION", font=("Imprint MT Shadow", 25, 'bold'),fg="#00008B" ,bg= "#63B8FF")
label.pack(padx=5, pady=5)

label_name = tk.Label(root, text="NAME",bg="#63B8FF", fg="#00008B", font=("Imprint MT Shadow", 18))
label_name.pack( padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.pack(padx=5, pady=5)

label_ic_number = tk.Label(root, text="IC NUMBER",bg="#63B8FF", fg="#00008B", font=("Imprint MT Shadow", 18))
label_ic_number.pack(padx=5, pady=5)
ic_number_entry = tk.Entry(root)
ic_number_entry.pack( padx=5, pady=5)

label_address= tk.Label(root, text="ADDRESS", bg="#63B8FF", fg="#00008B", font=("Imprint MT Shadow", 18))
label_address.pack(padx=10, pady=10)
address_entry = tk.Entry (root)
address_entry.pack( padx=5, pady=5)


label_gender= tk.Label(root, text="GENDER", bg="#63B8FF", fg="#00008B", font=("Imprint MT Shadow", 18))
label_gender.pack(padx=10, pady=10)
gender_entry = ttk.Combobox(root, values=["Male", "Female"])
gender_entry.pack(padx=5, pady=5)

label_age = tk.Label(root, text="AGE", bg="#63B8FF", fg="#00008B", font=("Imprint MT Shadow", 18))
label_age.pack(padx=5, pady=5)
age_entry = tk.Entry(root)
age_entry.pack(padx=5, pady=5)

submit_button = tk.Button(root, text="Submit", font=("Imprint MT Shadow", 15, 'bold'), bg='#6495ED', command=insert_data)
submit_button.place(x=100, y=500, width=80, height=50)

delete_button = tk.Button(root, text="Delete", font=("Imprint MT Shadow", 15, 'bold'), bg='#6495ED', command=delete_data)
delete_button.place(x=200,y=500, width=80, height=50 )

update_button = tk.Button(root, text="Update", font=("Imprint MT Shadow", 15, 'bold'), bg='#6495ED', command=update_data)
update_button.place(x=300, y=500,width=80, heigh=50 )

root.mainloop()