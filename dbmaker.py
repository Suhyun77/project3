import pandas as pd
import os 
import sqlite3


### read csv
EXCEL_PATH = os.path.join(os.getcwd(), 'excel/Childpark_data_DB.xlsx')
df = pd.read_excel(EXCEL_PATH)
df_list = df.values.tolist()

### DB 
DATABASE_PATH = os.path.join(os.getcwd(), 'Childpark_data.db')

conn = sqlite3.connect(DATABASE_PATH)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Entrance;")
cur.execute("""CREATE TABLE Entrance(
				Id INTEGER,
                Date TEXT,
                Weekend INTEGER,
                entrance_subtotal INTEGER,
                Avg_temperature INTEGER,
                Min_temperature INTEGER,
                Max_temperature INTEGER,
                Rainfall INTEGER,
                Holiday INTEGER);
			""")

for d1, d2, d3, d4, d5, d6, d7, d8, d9 in df_list:
    cur.execute("INSERT INTO Entrance (Id, Date, Weekend, entrance_subtotal, Avg_temperature, Min_temperature, Max_temperature, Rainfall, Holiday) VALUES (?,?,?,?,?,?,?,?,?);", (d1, d2, d3, d4, d5, d6, d7, d8, d9))

conn.commit()

