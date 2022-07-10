import cx_Oracle

connstr='system/Hero@007@localhost:1521/xepdb1'

conn=cx_Oracle.connect(connstr)
cur=conn.cursor()

sql_query='select * from college'
cur.execute(sql_query)
print(cur.fetchall())

cur.close()
conn.close()