
import os
import sqlite3


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
    temp = uname
    sql_command = "SELECT COUNT(*) FROM logins WHERE username='"+ uname +"' AND passwords='"+passwd+"'"
    data = c.execute(sql_command)
    
    for item in data:
        
        if item[0] == 1:
            print(item[0])
            clr_scr()
            master()

    conn.commit()
    conn.close()

def master():
    conn = sqlite3.connect("Passdatabase.db")
    c = conn.cursor()

    print("This session contains the details of OWASP TOP 10 vulnerabilities of 2022")
    print("Data source  : https://www.reflectiz.com/blog/owasp-top-ten-2022/")
    sql_command = """SELECT rowid,* FROM data
    """
    data = c.execute(sql_command)
    for item in data:
        print(item[0], item[1])
        print("     " + item[2])
    conn.commit()
    conn.close()
    

if __name__ == '__main__':
    welcome()
    print("Press any enter to continue...")
    input()
    clr_scr()
    uname = input("Enter user name  : ")
    passwd = input("Enter password  : ")
    pass_check(uname,passwd)


