#!/usr/bin/python3
""" Lists all the states from the database hbtn_0e_0_usa """
if __name__ == "__main__":
    import MySQLdb
    import sys

    host = "localhost"
    port = 3306
    passwd = sys.argv[2]
    db = sys.argv[3]
    user = sys.argv[1]
    db = MySQLdb.connect(host, user, passwd, db, port)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
                 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
