import mysql.connector
import bs4
import csv
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="iit123",
  database="easypcbuy"
)

# print(mydb)
my_cursor = mydb.cursor()


# my_cursor.execute("CREATE DATABASE easypcbuy") #database created
# my_cursor.execute("SHOW DATABASES") #command to show databases

# for db in my_cursor:
#     print(db)

# my_cursor.execute("DROP DATABASE sakila") #command for deleting databases
# my_cursor.execute("DROP DATABASE world")
#
# my_cursor.execute("SHOW DATABASES")
#
# for db in my_cursor:
#     print(db)


table_name = "ryans_processor"

# sql_add_table="CREATE TABLE "+table_name+" (product_name varchar(400),link varchar(400),price varchar(20))"
# my_cursor.execute(sql_add_table)

sql_insert = "INSERT INTO ryans_processor(product_name,link,price) VALUES (%s, %s, %s) "
file = open("Ryans\\ryans-processor.csv")
csv_read = csv.reader(file)
for row in csv_read:
    name = row[0]
    link = row[1]
    price = row[2][:-2]
    data = (name, link, price)
    my_cursor.execute(sql_insert, data)

mydb.commit()

