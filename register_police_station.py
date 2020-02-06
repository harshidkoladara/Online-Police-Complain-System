import sqlite3
import tkinter as tk

import mysql.connector

import database

conn = sqlite3.connect('local_police.db')
c = conn.cursor()

mydb = mysql.connector.connect(
    host='localhost', user='root', password='koladara'
)
mycursor = mydb.cursor()

try:
    mycursor.execute("USE police_complain")
except:
    print("DATABASE DOES NOT EXIST>>>")

rank_d, incharge_name_d, station_name_d, state_d, city_d, area_d, postal_code_d = "", "", "", "", "", "", ""
root = tk.Tk()


def register():
    global rank_d
    global incharge_name_d
    global station_name_d
    global state_d
    global city_d
    global area_d
    global postal_code_d
    select_city_variable = tk.StringVar(root)

    def submit_cmd():
        rank_d = variable_rank.get()
        incharge_name_d = entry_incharge_name.get()
        station_name_d = entry_station_name.get()
        state_d = variable_state.get()
        city_d = select_city_variable.get()
        area_d = entry_area.get()
        postal_code_d = entry_postal_code.get()

        sql = f"INSERT INTO `police_station` ( `rank`, `incharge_name`, `station_name`, `state`, `city`, `area`, `postalcode`) VALUES (\"{rank_d}\", \"{incharge_name_d}\", \"{station_name_d}\", \"{state_d}\", \"{city_d}\", \"{area_d}\", {int(postal_code_d)})"
        mycursor.execute(sql)
        c.execute(sql)
        mydb.commit()
        conn.commit()
        root.destroy()

    def config_entry(*a):
        rank_d = variable_rank.get()

    state_name_dict = dict(database.read_from_db(tablename='state'))
    state_name_list = list(state_name_dict.values())
    city_name_list = []

    root.title("Register Police Station")
    root.geometry("550x300")
    # root.state('zoomed')
    f1 = tk.Frame(root)
    f1.grid(row=0, column=0)
    f2 = tk.Frame(root)
    f2.grid(row=1, column=0)

    rank = ['DGP', 'CP', 'SDG', 'ADG', 'IG', 'DIG', 'JOINT CP', 'SSP', 'SDCP', 'SP', 'DCP', 'Dy.SP', 'ACP', 'ASP', 'PI',
            'SI', 'ASI']

    def ass(*a):
        return city_name_list

    def cities(*a):
        state_id = int()
        state = variable_state.get()
        for key, value in state_name_dict.items():
            if state == value:
                state_id = key

        city_names = list(database.read_from_db_condition(tablename='cities', state=state_id, column='city'))

        for x in city_names:
            city_name_list.append(x[0])

        select_city = tk.Label(f2, text="Select City", width=20, font=("bold", 10))
        select_city.grid(row=8, column=2)
        entry_city_w = tk.OptionMenu(f2, select_city_variable, *city_name_list)
        entry_city_w.grid(row=8, column=6)
        city_d = select_city_variable.get()

    registrationForm = tk.Label(f1, text="Register Police Station", width=20, font=("bold", 20))
    registrationForm.grid(row=1, column=1)

    name = tk.Label(f2, text="Station Incharge name", width=20, font=("bold", 10))
    name.grid(row=3, column=2)
    variable_rank = tk.StringVar(root)
    drop_incharge_rank = tk.OptionMenu(f2, variable_rank, *rank)
    drop_incharge_rank.grid(row=3, column=4)
    drop_incharge_rank.config(width=3, font=('Helvetica', 8))
    variable_rank.trace('w', config_entry)
    entry_incharge_name = tk.Entry(f2)
    entry_incharge_name.grid(row=3, column=6)
    rank_d = variable_rank.get()
    incharge_name_d = entry_incharge_name.get()

    station_name = tk.Label(f2, text="Station Name", width=20, font=("bold", 10))
    station_name.grid(row=4, column=2)
    entry_station_name = tk.Entry(f2)
    entry_station_name.grid(row=4, column=6)
    station_name_d = entry_station_name.get()

    # city = tk.Label(f2, text="Select City", width=20, font=("bold", 10))
    # city.grid(row=8, column=2)
    # variable_city = tk.StringVar(root)
    # entry_cityw = tk.OptionMenu(root, variable_city , *city_name_list)
    # entry_cityw.grid(row=8, column=6)
    # entry_cityw.config(width=10, font=('Helvetica', 12))

    states = tk.Label(f2, text="Select State", width=20, font=("bold", 10))
    states.grid(row=6, column=2)
    variable_state = tk.StringVar(f2)
    variable_state.set('GUJRAT')
    entry_state = tk.OptionMenu(f2, variable_state, *state_name_list)
    entry_state.grid(row=6, column=6)
    entry_state.config(width=10, font=('Helvetica', 12))
    variable_state.trace('w', cities)
    state_d = variable_state.get()

    area = tk.Label(f2, text="Area Name", width=20, font=("bold", 10))
    area.grid(row=10, column=2)
    entry_area = tk.Entry(f2)
    entry_area.grid(row=10, column=6)
    area_d = entry_area.get()

    postal_code = tk.Label(f2, text="Postal Code", width=20, font=("bold", 10))
    postal_code.grid(row=12, column=2)
    entry_postal_code = tk.Entry(f2)
    entry_postal_code.grid(row=12, column=6)
    postal_code_d = entry_area.get()

    submit_btn = tk.Button(f2, text='Submit', width=20, bg='brown', fg='white', command=submit_cmd)
    submit_btn.grid(row=16, column=7)

    root.mainloop()


if __name__ == "main":
    register()
