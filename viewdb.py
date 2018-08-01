import psycopg2 as p


def deleteTables():
    print 'clear database'


db = p.connect(database='log_database', user='admin2', password='admin', host='155.230.91.221', port='5432')
cursor = db.cursor()
cursor.execute("select * from logs_schema.logs_table")


#print all rows
print("-----------------------")
print("All rows: ")
rows = cursor.fetchall()
for row in rows:
    print(row)
print("end of all rows")
print("-----------------------")

