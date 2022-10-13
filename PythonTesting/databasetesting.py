import mysql.connector
mydb=mysql.connector.connect(host="117.236.76.142",user="root",password="mydb",database="vspmdemo")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("Show databases")
for db in mycursor:
    print(db)

#cursor=mydb.cursor()
mycursor.execute("select * from apm_admin")
#mycursor.execute("select * from apm_user")
for tb in mycursor:

    print(tb)