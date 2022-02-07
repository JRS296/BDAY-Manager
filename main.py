import email
import sqlite3
import csv
from tempfile import tempdir
import time
from unicodedata import name
import pandas as pd
import os.path
import smtplib
import datetime
from win10toast import ToastNotifier
import getpass

global GMAIL_ID  
global GMAIL_PWD 

GMAIL_ID = 'joeysamuel.gaming1@gmail.com'
GMAIL_PWD = ''
toast = ToastNotifier()

def sendEmail(to, sub, msg, g, p):
    gmail_obj = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_obj.starttls()    
    print("Current Gmail Account: " + g)
    val3 = input("Change user? [y/n]")
    if (val3 == 'Y' or val3 == 'y'):
        g = input("Enter Gmail User ID: ")
    p = getpass.getpass()
    gmail_obj.login(g, p)  
    gmail_obj.sendmail(g, to, f"Subject : {sub}\n\n{msg}")
    gmail_obj.quit() 
     
    print("Email sent to: " + str(to) + " Successfully, with subject " + str(sub) + " and message: " + str(msg))
    toast.show_toast("Email Sent Successfully! " , str(to)+" was sent an e-mail", threaded = True, icon_path = None, duration = 6)
    while toast.notification_active():
        time.sleep(0.1)

GMAIL_ID = 'joeysamuel.gaming1@gmail.com'
GMAIL_PWD = ''

con = sqlite3.connect("BDAY.db")
cur = con.cursor()
c1 = """CREATE TABLE IF NOT EXISTS BIRTHDAY(key INTEGER PRIMARY KEY, FIRST_NAME TEXT, LAST_NAME TEXT, DOB TEXT, PHONE NUMBER, EMAIL TEXT, INSTA TEXT)"""
cur.execute(c1)

file = open("test.csv")
print(file)
content = csv.reader(file)
cur.executemany(
    "INSERT INTO BIRTHDAY ( FIRST_NAME, LAST_NAME, DOB, PHONE, EMAIL, INSTA) VALUES ( ?, ?, ?, ?, ?, ?)", content)

count = 0
for row in cur.execute("SELECT * FROM BIRTHDAY"):
    count = count+1

y = 1
while (y == 1):
    print("\nWelcome to BDAY.exe v1.0")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("Enter 1 to send Birthday Wishes now!")
    print("Enter 2 to check Database")
    print("Enter 3 to Edit Database")
    print("Enter 4 to Update & download CSV file in current state")
    print("Enter x to Exit")
    val = input()
    print()

    if (val == '1'):
        print("Preparing Mail...")
        df = pd.read_sql_query("SELECT * from BIRTHDAY", con)
        today = datetime.datetime.now().strftime("%d.%m")
        yearNow = datetime.datetime.now().strftime("%d.%m.%Y")
        writeInd = []  

        print("Checking if there are any birthdays today...")
        for row in cur.execute("SELECT * FROM BIRTHDAY WHERE key != 1"):
            bday = bday2 = str(row[3])
            bday = bday[:-5]
            #print(bday)
            name_first = row[1]
            Email = row[5]
            
            if (today == bday):   
                msg = "Happy Birthday dear " + str(name_first) + "!! Have a great year ahead and may God bless! :)"
                print("Basic Template: ",msg)
                print("Name: ",name_first)
                print("Bday: ",bday2)
                print("Email: ",Email)
                sendEmail(Email, "Happy Birthday!!!", msg, GMAIL_ID, GMAIL_ID)  
                writeInd.append("Name: "+name_first+ " Date: "+today);   
                print()                              

    elif (val == '2'):
        #for row in cur.execute("SELECT * FROM BIRTHDAY"):
            #print(row)
        df = pd.read_sql_query("SELECT * from BIRTHDAY", con)
        print(df.head(100))
        print()

    elif (val == '3'):
        print("Enter 1 to Add New friend to database")
        print("Enter 2 to Delete Old friend from database")
        print("Enter 3 to Edit friend details from database")
        val2 = input()
        print()
        if (val2 == '1'):
            arr = []
            count += 1
            arr.append(input("Enter First Name: "))
            arr.append(input("Enter Last Name: "))
            arr.append(input("Enter DOB (DD/MM/YYYY): "))
            arr.append(input("Enter Phone No: "))
            arr.append(input("Enter Email: "))
            arr.append(input("Enter Instagram Handle: "))
            print(arr," Succesfully Inserted\n")
            cur.executemany("INSERT INTO BIRTHDAY ( FIRST_NAME, LAST_NAME, DOB, PHONE, EMAIL, INSTA) VALUES ( ?, ?, ?, ?, ?, ?)", (arr,))
        
        elif (val2 == '2'):
            df = pd.read_sql_query("SELECT * from BIRTHDAY", con)
            print(df.head(100))
            temp = (input("Enter key to be deleted: "))
            c1 = "DELETE FROM BIRTHDAY WHERE key = %d"
            adr = (temp,)
            cur.execute(c1,adr).fetchall()
            print("Successfully Deleted")
            count-=1
            print()
        
        elif (val2 == '3'):
            df = pd.read_sql_query("SELECT * from BIRTHDAY", con)
            print(df.head(100))
            temp = (input("Enter key to be Edited: "))
            arr = []
            arr.append(input("Enter First Name: "))
            arr.append(input("Enter Last Name: "))
            arr.append(input("Enter DOB (DD/MM/YYYY): "))
            arr.append(input("Enter Phone No: "))
            arr.append(input("Enter Email: "))
            arr.append(input("Enter Instagram Handle: "))
            print(arr," Succesfully Edited\n")
            c2 = "UPDATE BIRTHDAY (FIRST_NAME, LAST_NAME, DOB, PHONE, EMAIL, INSTA) VALUES ( ?, ?, ?, ?, ?, ?) WHERE key = %d"
            adr = (temp,)
            cur.executemany(c2, adr).fetchall()

        else:
            print("Invalid Choice!\n")

    elif (val == '4'):
        print("Getting Ready for Update...")
        #time.sleep(5)
        f = open('test.csv', 'w+')
        f.truncate()
        writer = csv.writer(f)
        for row in cur.execute("SELECT * FROM BIRTHDAY"):
            writer.writerow(row)
        print("Update Completed")
        f.close()
        temp = input("Download CSV File? [Y/N]")
        if (temp == 'Y' or temp=='y'):
            save_name = input("Enter name of file to be downloaded: ")
            save_path = 'C:/users/jonat/Downloads'
            completeName = os.path.join(save_path, save_name+".csv")   
            f2 = open(completeName, "w+")
            writer = csv.writer(f2)
            for row in cur.execute("SELECT * FROM BIRTHDAY"):
                writer.writerow(row)
            f2.close()
            print("Download Complete.")
        else:
            continue 

    elif (val == 'x'):
        print("Exiting...")
        break

    else:
        print("Invalid Entry, Try again.")


cur.execute("DROP TABLE BIRTHDAY").fetchall()
con.commit()
con.close()
