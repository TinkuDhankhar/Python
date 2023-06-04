import sqlite3
con = sqlite3.connect("sqlite.db")
Id = int(input("Enter you Id : - "))
ins = f"Delete from test where Id = {Id}"
con.execute(ins)
con.commit()
con.close()