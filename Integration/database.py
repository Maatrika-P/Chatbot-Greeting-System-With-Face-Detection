import sqlite3


def create_connection():

    connection = sqlite3.connect("memory.db")
    return connection

    create_connection()

def get_questionnaire():

    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * from questionnaire")

    for row in cur.fetchall():
        print(row)

get_questionnaire()

