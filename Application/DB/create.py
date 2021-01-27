import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies 
(Title TEXT, Director TEXT, Year INT)''')

cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Unknown', 1990)")
cursor.execute("SELECT * FROM Movies")

print(cursor.fetchall())

connection.commit()
connection.close()