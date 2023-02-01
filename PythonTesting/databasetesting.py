import mysql.connector
mydb=mysql.connector.connect(host="yuvicare.com",user="root",password="mariadb8080",database="balgopal")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("Show databases")
for db in mycursor:
    print(db)

#cursor=mydb.cursor()

mycursor.execute("select * from apm_user")
#mycursor.execute("select * from apm_user")
for tb in mycursor:
    print(tb)