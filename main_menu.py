import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = "", 
    database="driving_license"
)

mycursor=mydb.cursor()

def user_info():

    def insert_data():
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
            
        sql="INSERT INTO user_information (NAME,IC_NUMBER,ADDRESS,GENDER,AGE) VALUES(%s,%s,%s,%s,%s)"
        val=(label_name, label_ic_number, label_address, label_gender, label_age)
        
        mycursor.execute(sql,val)
        mydb.commit()

        messagebox.showinfo("Success", "Student information inserted successfully!")



    def delete_data():
        try:
            ic = ic_number_entry.get()
            
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="driving_license"
            )

            mycursor = mydb.cursor()

            delete_query = "DELETE FROM user_information WHERE IC_NUMBER = %s"

            mycursor.execute(delete_query, (ic,))
            mydb.commit()

            mycursor.close()
            mydb.close()

            messagebox.showinfo("Success", "Student information deleted successfully!")

            # Clear the entry widgets after deletion
            name_entry.delete(0, tk.END)
            ic_number_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
            gender_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            print(f"Error: {e}")


    def update_data():
        label_name = name_entry.get()
        label_address = address_entry.get()
        
        if label_name and label_address:

            try:
                with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="driving_license"
                ) as mydb:
                    with mydb.cursor() as mycursor:
                        update_query = "UPDATE user_information SET IC_NUMBER= %s, ADDRESS=%s"
                        mycursor.execute(update_query, (label_name,label_address))
                        mydb.commit()

                    messagebox.showinfo("Success", "Data updated successfully")
            except mysql.connector.Error as err:
                tk.messagebox.showerror("Error", f"Error: {err}")
        else:
            tk.messagebox.showwarning(title="Error", message="Name and ID are required.")


    root = tk.Tk()
    root.title("MAIN MENU")
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

    delete_button = tk.Button(root, text="Delete", font=("Imprint MT Shadow", 15, 'bold'), bg='#6495ED', command= delete_data)
    delete_button.place(x=200,y=500, width=80, height=50 )

    update_button = tk.Button(root, text="Update", font=("Imprint MT Shadow", 15, 'bold'), bg='#6495ED',command= update_data)
    update_button.place(x=300, y=500,width=80, heigh=50 )

def ins_info():  
    mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="driving_license"
            )

    cursor = mydb.cursor()

    def collect_data():
        number = number_entry.get()
        test = test_entry.get()
        gender = gender_type.get()
        license = license_type.get()

        print("Number:", number, "Test:", test, "Gender:", gender, "License:", license)
        print("----------------------------------------------------------------------------------------------")

        sql = "INSERT INTO instructor_information(number, test, gender, license) VALUES (%s, %s, %s, %s)"
        val = (number, test, gender, license)
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")

    def update_data():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="driving_license"
        )

        mycursor = mydb.cursor() 

        # Write the SQL update query based on your database structure
        sql = "UPDATE instructor_information SET test = %s, gender = %s, license = %s WHERE number = %s"
        #val = (test, gender, license, number)

        mycursor.execute(sql, )#val
        mydb.commit()
        print(cursor.rowcount, "record updated.")

    def delete_data():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="driving_license"
        )

        cursor = mydb.cursor()
    
        number = number_entry.get()
        test = test_entry.get()
        gender = gender_type.get()
        license = license_type.get()

            # Write the SQL update query based on your database structure
        sql = "DELETE instructor_information SET test = %s, gender = %s, license = %s WHERE number = %s"
        val = (test, gender, license, number)

        
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record deleted.")

    root = tk.Tk()
    root.title("MAIN MENU")
    root.geometry("500x600")
    root.configure(bg="#27408B")

    label = tk.Label(root, text='INSTRUCTOR INFORMATION', font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B',)
    label.pack(ipadx=6, ipady=6)

    label_number = tk.Label(text="Number Car:", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B',)
    label_number.pack(padx=5)
    number_entry = tk.Entry()
    number_entry.pack(pady=10)

    label_test = tk.Label(text="Test:", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B',)
    label_test.pack(padx=5)
    test_entry = tk.Entry()
    test_entry.pack(pady=10)

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

def lic_pay():

    def collect_data():
        licensetype= license_type.get()
        extraclass= extra_class.get()
        paymenttype = payment_type.get()
        
        print("License Type", licensetype,"Extra Class",extraclass, "Payment Type", paymenttype)
        print("----------------------------------------------------------------------------------------------")

        sql= "INSERT INTO license_payment(LICENSE_TYPE,EXTRA_CLASS,PAYMENT_TYPE ) VALUES (%s,%s,%s)"
        val= ( licensetype, extraclass, paymenttype)

        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print("Data inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()

            extraclass= int(extra_class.get())

        prices= {
            "MANUAL CAR": 1300,
            "AUTO CAR" : 1500,
            "MOTORCYCLE": 450,
            "CAR AND MOTORCYCLE": 1800,
        }

        prices1= {
            '1': 10,
            '2': 20,
            '3': 30,
            '4': 40,
        }

        

        total_payment= prices[licensetype] + prices1[str(extraclass)]

        output_label.config(text=f"TOTAL PAYMENT: RM{total_payment}")
        output_label.pack(pady=5)    

        
    def update_data():
        mydb=mysql.connector.connect(
            host="localhost",
            user= "root",
            password= "",
            database= "driving_license"
        )

        licensetype= license_type.get()
        extraclass= extra_class.get()
        paymenttype = payment_type.get()

        cursor= mydb.cursor()

        print("License Type", licensetype,"Extra Class",extraclass, "Payment Type", paymenttype)
        print("----------------------------------------------------------------------------------------------")

        sql= "UPDATE license_payment(LICENSE_TYPE,EXTRA_CLASS, PAYMENT_TYPE) VALUES (%s,%s,%s)"
        val= ( licensetype, extraclass, paymenttype)
        
        
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record updated.")

    def delete_data():
        mydb=mysql.connector.connect(
            host="localhost",
            user= "root",
            password= "",
            database= "driving_license"
        )

        licensetype= license_type.get()
        extraclass= extra_class.get()
        paymenttype = payment_type.get()

        mycursor= mydb.cursor()

        print("License Type", licensetype,"Extra Class",extraclass, "Payment Type", paymenttype)
        print("----------------------------------------------------------------------------------------------")

        sql= "DELETE FROM license_payment(LICENSE_TYPE,EXTRA_CLASS, PAYMENT_TYPE )VALUES (%s,%s, %s)"
        val= ( licensetype, extraclass, paymenttype)
        
  
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record deleted.")

    root = tk.Tk()
    root.title("MAIN MENU")
    root.geometry("500x600")
    root.configure(bg="#27408B")

    label=tk.Label(root, text='LICENSE PAYMENT', font= ("Input Mono",30,"bold"),fg='#00008B', bg='#63B8FF')
    label.pack(padx=20, pady=10)

    frame= tk.Frame (root, bg='blue')
    frame.pack()

    info = tk.LabelFrame(frame, text="", bg='blue')
    info.grid(row=0, column=1, sticky= "News", padx=1, pady=1)

    #license type
    license_label=tk.Label(info, text= "LICENSE TYPE", bg='#6495ED', font=("Times New Roman",15, "bold"))
    license_label.pack(padx=5)

    license_type= tk.StringVar (root)
    license_type.set ("Select License")
    license_dropdown= tk.OptionMenu(info, license_type ,"MANUAL CAR", "AUTO CAR", "MOTORCYCLE", "CAR AND MOTORCYCLE")
    license_dropdown.pack(pady=10)

    #extra class
    extra_label=tk.Label( info, text= "EXTRA CLASS", bg='#6495ED', font=("Times New Roman",15, "bold"))
    extra_label.pack(padx=5)

    extra_class= tk.StringVar (root)
    extra_class.set ("Select Extra Class")
    extra_dropdown= tk.OptionMenu(info, extra_class,"1","2","3","4")
    extra_dropdown.pack(pady=10)


    # payment method
    payment_label= tk.Label(info, text="PAYMENT METHOD", bg='#6495ED', font= ("Times New Roman",15, "bold"))
    payment_label.pack(padx=5)

    payment_type= tk.StringVar(root)
    payment_type.set ("Select Payment Method")
    payment_dropdown= tk.OptionMenu(info, payment_type,"cash", "card","online banking") 
    payment_dropdown.pack(pady=5)

    #SAVE BUTTON 
    payment_total= tk.Button(info, text= "TOTAL PAYMENT", font= ("Times New Roman", 15, "bold"),bg='#6495ED', command=collect_data)
    payment_total.pack(pady=10)

    #output
    label= tk.Label(info, text='TOTAL', bg='#6495ED',font=("Times New Roman", 15, "bold"))
    label.pack(ipadx=10,ipady=10)

    output_label= tk.Label(info, text="")
    output_label.pack()

    button_update = tk.Button(root, text="Update", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B', command=update_data)
    button_update.pack(pady=10)

    button_delete = tk.Button(root, text="Delete", font= ("Imprint MT Shadow", 15, "bold"),bg='#6495ED',fg='#00008B', command=delete_data)
    button_delete.pack(pady=10)


# Tkinter GUI
root = tk.Tk()
root.title("MAIN MENU")
root.geometry("500x600")
root.configure(bg="#27408B")

label = tk.Label(root, text="WELCOME TO DRIVING\n SDN BHD", font=("Imprint MT Shadow",25, 'bold'),fg="#00008B" ,bg= "#63B8FF")
label.pack(padx=5, pady=5)

label = tk.Label(root, text="REGISTRATION PAGE", font=("Imprint MT Shadow",25, 'bold'),fg="#00008B" ,bg= "#63B8FF")
label.pack(padx=5, pady=5)

User_button = tk.Button(root, text="USER", font=("Imprint MT Shadow", 20, 'bold'), bg='white', activebackground='blue', command=user_info)
User_button.pack(padx=5,pady=50)

Instructor_button = tk.Button(root, text="INSTRUCTOR", font=("Imprint MT Shadow", 20, 'bold'), bg='white', activebackground='blue', command=ins_info)
Instructor_button.pack(padx=5,pady=50)

Payment_button = tk.Button(root, text="PAYMENT", font=("Imprint MT Shadow", 20, 'bold'), bg='white', activebackground='blue', command=lic_pay)
Payment_button.pack(padx=5, pady=50)



root.mainloop()