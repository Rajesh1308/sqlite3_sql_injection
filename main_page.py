import sqlite3

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
    