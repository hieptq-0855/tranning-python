import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("""CREATE TABLE IF NOT EXISTS customers
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255)
    )""")
