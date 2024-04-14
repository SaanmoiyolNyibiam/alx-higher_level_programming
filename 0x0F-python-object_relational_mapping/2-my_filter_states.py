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
    state_name = sys.argv[4]
    db = MySQLdb.connect(host, user, passwd, db, port)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY id ASC".format(state_name))
    output = cur.fetchall()
    for row in output:
        print(row)

    cur.close()
    db.close()
