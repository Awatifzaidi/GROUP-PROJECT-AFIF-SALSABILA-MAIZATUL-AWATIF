import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Page3(tk.Frame):
    def __init__(self, root, show_main_menu):
        super().__init__(root, width=400, height=300)
        label = tk.Label(self, text="Page 3", font=('Helvetica', 18))
        label.pack(pady=20)

        back_button = tk.Button(self, text="Back to Main Menu", command=show_main_menu)
        back_button.pack(pady=10)

#mydb=mysql.connector.connect(
    #host="localhost",
    #user= "root",
    #password= "",
    #database= "license_payment"
#)

#mycursor= mydb.cursor()

def collect_data():
     
    licensetype= license_type.get()
    extraclass= extra_class.get()
    paymenttype = payment_type.get()
    
    
    
    print("License Type", licensetype,"Extra Class",extraclass, "Payment Type", paymenttype)
    print("----------------------------------------------------------------------------------------------")

    #sql= "INSERT INTO license_payment(LICENSE_TYPE,EXTRA_CLASS, PAYMENT_TYPE, PAYMENT_TOTAL ) VALUES (%s,%s, %s,)"
   # val= ( licensetype, extraclass, paymenttype)

    #try:
        #mycursor.execute(sql, val)
       # mydb.commit()
        #print("Data inserted successfully!")
    #except mysql.connector.Error as err:
        #print(f"Error: {err}")
        #mydb.rollback()

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

    

    total_payment= prices[licensetype] + prices1[extraclass]

    output_label.config(text=f"TOTAL PAYMENT: RM{total_payment}")
    output_label.pack(pady=5)

def update_data():
    #mydb=mysql.connector.connect(
    #   host="localhost",
    #   user= "root",
    #   password= "",
    #  database= "license_payment"
 #)


  #mycursor= mydb.cursor()
    
    licensetype= license_type.get()
    extraclass= extra_class.get()
    paymenttype = payment_type.get() 

    print("License Type", licensetype,"Extra Class",extraclass, "Payment Type", paymenttype)
    print("----------------------------------------------------------------------------------------------")

    #sql= "UPDATE INTO license_payment(LICENSE_TYPE,EXTRA_CLASS, PAYMENT_TYPE, PAYMENT_TOTAL ) VALUES (%s,%s, %s,)"
   # val= ( licensetype, extraclass, paymenttype)
    
    # Execute the update query
    #cursor.execute(sql, val)
    #mydb.commit()
    #print(cursor.rowcount, "record updated.")

def delete_data():
    #mydb=mysql.connector.connect(
    #   host="localhost",
    #   user= "root",
    #   password= "",
    #  database= "license_payment"
 #)


  #mycursor= mydb.cursor()
    
    licensetype= license_type.get()
    extraclass= extra_class.get()
    paymenttype = payment_type.get() 

    print("License Type", licensetype,"Extra Class",extraclass, "Payment Type", paymenttype)
    print("----------------------------------------------------------------------------------------------")

    #sql= "DELETE INTO license_payment(LICENSE_TYPE,EXTRA_CLASS, PAYMENT_TYPE, PAYMENT_TOTAL ) VALUES (%s,%s, %s,)"
   # val= ( licensetype, extraclass, paymenttype)
    
    # Execute the update query
    #cursor.execute(sql, val)
    #mydb.commit()
    #print(cursor.rowcount, "record deleted.")


#MAIN WINDOW
root=tk.Tk()
root.title("DRIVING LICENSE")
root.geometry('500x600')
root.configure(bg='#63B8FF')

#PAGE TITLE 
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

root.mainloop()

#mycursor.close()
#mydb.close()
