import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', user='root', password='koladara'
)
mycursor = mydb.cursor()

try:
    mycursor.execute("USE police_complain")
except:
    print("DATABASE DOES NOT EXIST>>>")


def read_from_db(tablename, column='*'):
    sql = f"SELECT {column} FROM {tablename}"
    mycursor.execute(sql)
    return mycursor.fetchall()


def read_from_db_condition(tablename, state, column='*'):
    sql = f"SELECT {column} FROM {tablename} WHERE state_id = \'{state}\'"
    mycursor.execute(sql)
    return mycursor.fetchall()


def insert_station(rank_d, incharge_name_d, station_name_d, state_d, city_d, area_d, postal_code_d):
    pos = int(postal_code_d)
    sql = f"INSERT INTO `police_station` ( `rank`, `incharge_name`, `station`, `state`, `city`, `area`, `postalcode`) VALUES (\'{rank_d}\', \'{incharge_name_d}\', \'{station_name_d}\', \'{state_d}\', \'{city_d}\', \'{area_d}\', \'{pos}\')\'"
    mycursor.execute(sql)


if __name__ == "main":
    read_from_db()
