import mysql.connector

con=mysql.connector.connect(host='bb5gus91xfx00gmzjktw-mysql.services.clever-cloud.com',user='uasnkhqhmbiorpfv',password='foxAyuEDdQ59uREA8X3T',database='bb5gus91xfx00gmzjktw')
curs=con.cursor()
'''
curs.execute("alter table Books add Review varchar(500)")
con.commit()
print("altered")
'''

cd=int(input("Enter Bookcode: "))
curs.execute("select*from Books where Bookcode=%d"%cd)
data=curs.fetchall()
if data:
    rev=input("Review: ")

    curs.execute("update Books set Review='%s' where bookcode=%d"%(rev,cd))
    con.commit()
    print("Review updated successfully")
else:
    print("Book not found")
    