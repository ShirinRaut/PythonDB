import mysql.connector

con=mysql.connector.connect(host='bb5gus91xfx00gmzjktw-mysql.services.clever-cloud.com',user='uasnkhqhmbiorpfv',password='foxAyuEDdQ59uREA8X3T',database='bb5gus91xfx00gmzjktw')
curs=con.cursor()

curs.execute("select * from Books")
data=curs.fetchall()

for rec in data:
        print("Bookcode      :%d"%rec[0])
        print("Bookname      :%s"%rec[1])
        print("Category      :%s"%rec[2])
        print("Author        :%s"%rec[3])
        print("Publication   :%s"%rec[4])
        print("Edition       :%s"%rec[5])
        print("Price         :%d"%rec[6])
        print('-'*50)
con.close()