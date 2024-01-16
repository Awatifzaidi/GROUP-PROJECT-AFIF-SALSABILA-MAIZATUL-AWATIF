import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Page2(tk.Frame):
    def __init__(self, root, show_main_menu):
        super().__init__(root, width=400, height=300)
        label = tk.Label(self, text="Page 2", font=('Helvetica', 18))
        label.pack(pady=20)

        back_button = tk.Button(self, text="Back to Main Menu", command=show_main_menu)
        back_button.pack(pady=10)

def collect_data():
    number = number_entry.get()
    test = test_entry.get()
    gender = gender_type.get()
    license = license_type.get()

    print("Number:", number, "Test:", test, "Gender:", gender, "License:", license)
    print("----------------------------------------------------------------------------------------------")

    
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="driving_license"
        )

    cursor = mydb.cursor()
    sql = "INSERT INTO instructor_data (number, test, gender, license) VALUES (%s, %s, %s, %s)"
    val = (number, test, gender, license)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")

def update_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="driving_license"
    )

    cursor = mydb.cursor()
    
    number = number_entry.get()
    test = test_entry.get()
    gender = gender_type.get()
    license = license_type.get()

    # Write the SQL update query based on your database structure
    sql = "UPDATE instructor_data SET test = %s, gender = %s, license = %s WHERE number = %s"
    val = (test, gender, license, number)

    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record updated.")

def delete_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="driving_license"
    )

    cursor = mydb.cursor()
    
    number = number_entry.get()
    test = test_entry.get()
    gender = gender_type.get()
    license = license_type.get()

    # Write the SQL update query based on your database structure
    sql = "DELETE instructor_data SET test = %s, gender = %s, license = %s WHERE number = %s"
    val = (test, gender, license, number)

    
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record deleted.")
    

root = tk.Tk()
root.title("MySQL Database with Tkinter")
root.geometry("500x600")
root.configure(bg="blue")

label = tk.Label(root, text='INSTRUCTOR INFORMATION', font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B',)
label.pack(ipadx=6, ipady=6)

frame = tk.Frame(root, bg="blue")
frame.pack()

label_number = tk.Label(text="Number Car:", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B',)
label_number.pack()
number_entry = tk.Entry()
number_entry.pack()

label_test = tk.Label(text="Test:", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B',)
label_test.pack()
test_entry = tk.Entry()
test_entry.pack()

label_gender = tk.Label(text="Gender:", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B',)
label_gender.pack()
gender_type = tk.StringVar(root)
gender_type.set("Select gender")
gender_dropdown = tk.OptionMenu(root, gender_type, "Male", "Female")
gender_dropdown.pack(pady=10)

label_license = tk.Label(text="License's Type:", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B',)
label_license.pack()
license_type = tk.StringVar(root)
license_type.set("Select your License's Type")
license_dropdown = tk.OptionMenu(root, license_type, "Auto", "Manual", "Motorcycle")
license_dropdown.pack(pady=10)

button_done = tk.Button(root, text="Done", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B', command=collect_data)
button_done.place(x=100, y=300, width=80, height=50)

button_update = tk.Button(root, text="Update", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B', command=update_data)
button_update.place(x=200, y=300, width=80, height=50)

button_delete = tk.Button(root, text="Delete", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B', command=delete_data)
button_delete.place(x=300, y=300, width=80, height=50)

root.mainloop()

