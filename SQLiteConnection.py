import sqlite3
con = sqlite3.connect("sqlite.db") # create same root path
con.execute('''
create table test(
id int auto_increment primary key,
name nvarchar(100)
)
''')
con.close()
# download DB browser and install it's free of cost available for you
