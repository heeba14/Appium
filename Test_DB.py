import pymysql

db = pymysql.connect("localhost", "root", "mysql123", "python")

cursor = db.cursor()

sql = '''SELECT * FROM Profile'''
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   print(("Number of rows: %d") % (len(results))) #to fetch number of rows
   #To validate and print first row
   if results[0][0] =='Heeba' and results[0][1] =='Kawoosa' and results[0][2] == 22:
       print(results[0])
   else:
          print("Record Not Found")

except:
   print ("Error: unable to fetch data")

db.close()