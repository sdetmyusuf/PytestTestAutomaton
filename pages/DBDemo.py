import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="APIDevelop",
  user="root",
  password="Rootpassword@143")

print(mydb.is_connected())

cursr = mydb.cursor()
cursr.execute("SHOW TABLES")
result = cursr.fetchall()

# print("Printing first user record")
# for row in result:
#     print(row)


# cursr.execute("select * from Storage3")
# resultstr = cursr.fetchall()
# print("Printing================")
# print(resultstr)

# cursr.execute("INSERT INTO Storage3 values('selenium 4.0','qwer121','qwert','121','Mohd Yusuf')")
# mydb.commit()
# cursr.execute("select * from Storage3")
# resultstr = cursr.fetchall()
# print("Printing================")
# print(resultstr)


# print("Total number of rows in users is: ", cursr.rowcount)
# print("Printing each user record")
# for row in result:
#     print(row)

# cursr.execute("select * from Storage3 where book_name = 'selenium 4.0'")
query = "update Storage3 set book_name = %s where aisle = %s"
data = ("AI New Version", "1202")
cursr.execute(query, data)
mydb.commit()

