#!C:/Users/Swachandrika/AppData/Local/Programs/Python/Python39/python.exe
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    port = "3307",
    user = "root",
    password = "root",
    database = "mydb"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE DeptSales(ClientName varchar(25), OrderID varchar(20),Price int)")
import random
import cgi
# create instance of fieldStorage
form = cgi.FieldStorage()
# get data from fields
n = form.getvalue('name')
if form.getlist("items"): items = form.getlist("item")
else:items = "Not selected!"
if form.getlist("qty"): qty = form.getlist("qty")
else:qty = "Not selected!"

p = 0
for i in items:
    for q in qty:
        p +=q

print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h4> Thank You for Shopping!</h4>")
sql=("INSERT INTO DeptSales VALUES (%s,%s,%s)")
od = random.randint(1,100)
val=(n,od,p)
mycursor.execute(sql,val)
mydb.commit()
print("</body></html>")
print("Record inserted.")
