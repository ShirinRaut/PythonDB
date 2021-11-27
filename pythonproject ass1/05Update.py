import mysql.connector

con=mysql.connector.connect(host='bb5gus91xfx00gmzjktw-mysql.services.clever-cloud.com',user='uasnkhqhmbiorpfv',password='foxAyuEDdQ59uREA8X3T',database='bb5gus91xfx00gmzjktw')
curs=con.cursor()

cd=int(input("Enter Bookcode: "))
pr=float(input("Enter price to change: "))  

curs.execute("select * from Books where bookcode=%d"%cd)
data=curs.fetchall()
if data:
    curs.execute("update Books set price=%.2f where Bookcode=%d"%(pr,cd))
    con.commit()
    print("price is changed")

else:    
    print("Book doesnot exist")

con.close()    
