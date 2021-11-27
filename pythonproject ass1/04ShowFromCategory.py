import mysql.connector

con=mysql.connector.connect(host='bb5gus91xfx00gmzjktw-mysql.services.clever-cloud.com',user='uasnkhqhmbiorpfv',password='foxAyuEDdQ59uREA8X3T',database='bb5gus91xfx00gmzjktw')
curs=con.cursor()

ct=input("Enter category of books: ")
curs.execute("select * from Books where Category='%s'"%ct)

data=curs.fetchall()

if data:
    for rec in data:
        print(rec[1])
        print('-'*30)

if not data:
    print("Book Not Found")

con.close()