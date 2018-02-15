import pymysql

db = pymysql.connect("localhost", "root", "mysql123", "python")
    
"""Create Table"""
def create_table():
    #db = pymysql.connect("localhost", "root", "mysql123", "python")
    cursor = db.cursor()
    #cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    sql = """CREATE TABLE Number (
    FIRST_NAME  TEXT NOT NULL,
    LAST_NAME  TEXT,
    AGE INT )"""
    cursor.execute(sql)
    #db.close()
    
"""Insert Table"""
def insert_table():
    #db = pymysql.connect("localhost", "root", "mysql123", "python")

    cursor = db.cursor()

    sql = """INSERT INTO Profile(FIRST_NAME,
       LAST_NAME, AGE)
       VALUES ('Heeba', 'Kawoosa', 24)"""
    try:

        cursor.execute(sql)

        db.commit()
    except:

        db.rollback()

    #db.close()

""" Read Table """
def read_table():
    #db = pymysql.connect("localhost", "root", "mysql123", "python")

    cursor = db.cursor()

    sql = '''SELECT * FROM Profile'''
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

    except:
        print("Error: unable to fetch data")
        #db.close()

""" Update Table """
def update_table():
    #db = pymysql.connect("localhost", "root", "mysql123", "python")

    cursor = db.cursor()

    sql = """UPDATE Profile SET AGE = AGE -1
                              WHERE First_name = 'Heeba'"""
    try:

        cursor.execute(sql)

        db.commit()
    except:

        db.rollback()

    #db.close()


create_table()
insert_table()
read_table()
update_table()

db.close()