import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost", 
                            user="root", 
                            password="password",
                            db = "project")
    c = conn.cursor()

    return c, conn