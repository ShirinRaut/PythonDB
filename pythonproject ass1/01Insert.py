import mysql.connector

con=mysql.connector.connect(host='bb5gus91xfx00gmzjktw-mysql.services.clever-cloud.com',user='uasnkhqhmbiorpfv',password='foxAyuEDdQ59uREA8X3T',database='bb5gus91xfx00gmzjktw')
curs=con.cursor()

try:
    cd=int(input("Enter a book code    : "))
    nm=input("Enter Book name          : ")
    ct=input("Enter category of book   : ")
    at=input("Enter name of Author     : ")
    pb=input("Enter Publication        : ")
    ed=input("Enter edition            : ")
    pr=float(input("Enter price of book: "))
     
    curs.execute("insert into Books values(%d,'%s','%s','%s','%s','%s',%.2f)"%(cd,nm,ct,at,pb,ed,pr)) 
    con.commit()
    print("Book added successfully")
    con.close()

except:
    print("Invalid input.Please try some other values")
