import sqlite3

connection = sqlite3.connect("itstep_22.sl3", 5)

cur = connection.cursor()

print(connection)
print(cur)

cur.execute("INSERT INTO first_table (name) VALUES ('Vasyul');")
connection.commit()

connection.close()