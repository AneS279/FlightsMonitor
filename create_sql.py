import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('latam.db')
 

# cursor object
cursor_obj = connection_obj.cursor()
 
cursor_obj.execute("DROP TABLE IF EXISTS pricesLatam")
 
# Creating table
table = """ CREATE TABLE pricesLatam (
            day datetime NOT NULL,
            price FLOAT NOT NULL,
            cia varchar(50) NOT NULL,
            PRIMARY KEY(day, cia)
        ); """
 
cursor_obj.execute(table)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()