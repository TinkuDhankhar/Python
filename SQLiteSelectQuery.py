import sqlite3
con = sqlite3.connect("sqlite.db")
select = '''
select * from test limit 0,10
'''
data = con.execute(select)
con.commit()
for i in data:
    print(i)
con.close()
