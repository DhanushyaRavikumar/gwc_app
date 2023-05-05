import mysql.connector

mydb = mysql.connector.connect(host="34.67.234.188", user="gwcapp", passwd="gwcapp")

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE gwcpmp")

#mycursor.execute("SHOW DATABASES")
#for db in mycursor:
#    print(db)
