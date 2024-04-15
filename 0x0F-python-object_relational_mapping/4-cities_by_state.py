#!/usr/bin/python3
"""
    Lists all the states from the database hbtn_0e_0_usa,
    where name matches the argument,
    and is safe from MySQL injections.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    import re

    host = "localhost"
    port = 3306
    passwd = sys.argv[2]
    db = sys.argv[3]
    user = sys.argv[1]
    db = MySQLdb.connect(host, user, passwd, db, port)
    cur = db.cursor()
    # use a parameterized query to prevent MySQL injection
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id=states.id")
    output = cur.fetchall()
    for row in output:
        print(row)

    cur.close()
    db.close()
