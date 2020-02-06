import sqlite3

from sqlite3 import Error


def sql_connection():
    try:

        con = sqlite3.connect('local_police.db')
        return con

    except Error:

        print(Error)


def sql_table(con):
    cursorObj = con.cursor()
    # cursorObj.execute('insert into data VALUES(1,0," "))')
    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS police_station(id int AUTO_INCREMENT, rank varchar(10), incharge_name varchar(32), station_name varchar(50), state varchar(32), city varchar(32), area varchar(32), postalcode int, primary key(id))")
    a = cursorObj.execute("SELECT station_name FROM police_station")
    return a.fetchall()
