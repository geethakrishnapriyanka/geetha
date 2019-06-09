import sqlite3
conn=sqlite3.connect('test.db')
print("opened database successfully")
conn.execute("delete from company where id=2")
conn.commit()
print("total numberb of rows updated:",conn.total_changes)
cursor=conn.execute('''select id,name,address,salary from company''')
for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("address=",row[2])
    print("salary=",row[3])
print("operation done successfully")
conn.close()
