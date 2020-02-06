import register_police_station
from mainconnection import *

con = sql_connection()

what = sql_table(con)

if (not what):
    register_police_station.register()
    cursorObj = con.cursor()

    # cursorObj.execute('update data set num=1 where id=1')
    # con.commit()
else:
    con = sql_connection()

    cursorObj = con.cursor()

    # cursorObj.execute('select address from data where id=1')
    rows = cursorObj.fetchall()

    for row in rows:
        print(row[0])

    con.commit()
