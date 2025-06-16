import sqlite3
conn = sqlite3.connect('records.db')
c = conn.cursor()
def CreateTable():
	listOfTables = c.execute("""SELECT * FROM records""").fetchall()
 
	if listOfTables == []:
		print('Table not found!')
		c.execute("CREATE TABLE records(name, author,serie, genre, favourite character, rate, notes, image)")
	else:
		print('Table found!')
