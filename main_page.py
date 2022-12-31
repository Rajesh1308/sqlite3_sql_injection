import sqlite3

def master():
    conn = sqlite3.connect("Passdatabase.db")
    c = conn.cursor()
    sql_command = """SELECT rowid,* FROM data
    """
    data = c.execute(sql_command)
    for item in data:
        print(item[0], item[1])
        print("     " + item[2])
    conn.commit()
    conn.close()
    