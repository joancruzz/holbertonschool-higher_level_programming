#!/usr/bin/python3
'''
lists all states in database
'''

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=330, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    db.close()
    rows = cur.fetchall()
for row in rows:
    print("{}".format(row))
