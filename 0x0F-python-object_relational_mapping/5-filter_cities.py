#!/usr/bin/python3
"""
    Takes in the name of a state as an argument and lists
    all the cities of that state from the database hbtn_0e_0_usa,
    and is safe from MySQL injections.
"""
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
    # use a parameterized query to prevent MySQL injection
    cur.execute("SELECT cities.name\
                FROM cities\
                INNER JOIN states ON cities.state_id=states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (state_name,))
    output = cur.fetchall()
    len = len(output)
    for index, row in enumerate(output):
        if (index + 1 == len):
            print(row[0])
        else:
            print(row[0], end=", ")

    cur.close()
    db.close()
