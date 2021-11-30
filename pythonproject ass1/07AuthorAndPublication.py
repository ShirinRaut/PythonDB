import mysql.connector

con=mysql.connector.connect(host='bb5gus91xfx00gmzjktw-mysql.services.clever-cloud.com',user='uasnkhqhmbiorpfv',password='foxAyuEDdQ59uREA8X3T',database='bb5gus91xfx00gmzjktw')
curs=con.cursor()

print("Name the Author And Publication: ")
at=input("Author: ")
pb=input("Publication: ")

curs.execute("select * from Books where Author='%s' and Publication='%s'"%(at,pb))
data=curs.fetchall()
if data:
    print(data)
else:
    print("Book is not available")  
