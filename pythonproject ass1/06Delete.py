import mysql.connector

con=mysql.connector.connect(host='bb5gus91xfx00gmzjktw-mysql.services.clever-cloud.com',user='uasnkhqhmbiorpfv',password='foxAyuEDdQ59uREA8X3T',database='bb5gus91xfx00gmzjktw')
curs=con.cursor()

cd=int(input("Enter Bookcode: "))
curs.execute("select * from Books where Bookcode=%d"%cd)
data=curs.fetchall()
if data:
    for rec in data:
        print("Bookcode      :%d"%rec[0])
        print("Bookname      :%s"%rec[1])
        print("Category      :%s"%rec[2])
        print("Author        :%s"%rec[3])
        print("Publication   :%s"%rec[4])
        print("Edition       :%s"%rec[5])
        print("Price         :%d"%rec[6])
        
    
    ask=input("Do you want to delete this book from list ? ")
    if ask.lower()=="yes":
        curs.execute("delete from Books where Bookcode=%d"%cd)
        con.commit()
        print("Book deleted successfully")
    else:
        print("OK")
 
if not data:
    print("Book not found")

con.close()       