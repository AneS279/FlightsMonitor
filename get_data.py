import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('latam.db')
# cursor object
cursor_obj = connection_obj.cursor()
# Creating table
table = """ SELECT * FROM pricesLatam"""
cursor_obj.execute(table)
output = cursor_obj.fetchall()

df = pd.DataFrame(output, columns=['date', 'price', 'cia'])
# Close the connection
connection_obj.close()

df.plot(x="date", y="price")
plt.show()
