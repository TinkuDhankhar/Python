import sqlite3
con = sqlite3.connect("sqlite.db")
ins = '''
insert into test values(1,'test')
'''
con.execute(ins)
con.commit()
con.close()