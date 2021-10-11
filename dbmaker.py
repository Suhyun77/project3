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
                Adults_guest INTEGER,
                Youth_guest INTEGER,
                Child_guest INTEGER, 
                Foreigner_guest INTEGER,
                Group_guest INTEGER,
                Subtotal INTEGER,
                Avg_temperature INTEGER,
                Min_temperature INTEGER,
                Max_temperature INTEGER,
                rainfall INTEGER);
			""")

for d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13 in df_list:
    cur.execute("INSERT INTO Entrance (Id, Date, Weekend, Adults_guest, Youth_guest, Child_guest, Foreigner_guest, Group_guest, Subtotal, Avg_temperature, Min_temperature, Max_temperature, rainfall) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);", (d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13))

conn.commit()

# XgBoost Model

