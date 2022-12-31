
import os
import sqlite3
import getpass
import main_page as mp


def welcome():
    print("================================================================")
    print("=         Welcome to Demo on SQL injection with sqlite3        =")
    print("================================================================")

    print("\n\nThe projects aims to provide a hands on experience on sql injection")
    print("Here in the password section you can execute sql injection to gain access the data inside the project")
    print("Inside the project, in the search option you can perform union attack and view all the user ID and passwords")
    print("All the best and have a good testing\n\n")

def clr_scr():
    os.system('cls')
    print("================================================================")
    print("=         Welcome to Demo on SQL injection with sqlite3        =")
    print("================================================================")

    
def pass_check(uname,passwd):
    conn = sqlite3.connect("Passdatabase.db")
    c = conn.cursor()
    sql_command = "SELECT * FROM logins WHERE username='"+uname +"' AND passwords='"+passwd+"'"
    data = c.execute(sql_command)
    
    for item in data:
        print(item[0])
        if item[0] == uname:
            clr_scr()
            mp.master()

    conn.commit()
    conn.close()

if __name__ == '__main__':
    welcome()
    print("Press any enter to continue...")
    input()
    clr_scr()
    unam = input("Enter user name : ")
    passwd = getpass.getpass()
    pass_check(unam,passwd)


