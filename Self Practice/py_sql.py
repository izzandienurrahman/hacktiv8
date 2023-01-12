import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin",
  database="ftds"
)


def insert_data(db):
  name = input("Name: ")
  address = input("Address: ")
  val = (name, address)
  cursor = db.cursor()
  sql = "INSERT INTO student (name, address) VALUES (%s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data added".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM student"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("No data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  student_id = input("Select student id> ")
  name = input("New Name: ")
  address = input("New Address: ")

  sql = "UPDATE student SET name=%s, address=%s WHERE student_id=%s"
  val = (name, address, student_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data changed".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  student_id = input("Select student id> ")
  sql = "DELETE FROM student WHERE student_id=%s"
  val = (student_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data deleted".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Keyword: ")
  sql = "SELECT * FROM student WHERE name LIKE %s OR address LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("No Data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== H8 Py MySQL Exercise ===")
  print("1. Insert Data")
  print("2. Show Data")
  print("3. Update Data")
  print("4. Delete Data")
  print("5. Search Data")
  print("0. Exit")
  print("------------------")
  menu = input("Select menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Wrong Input")


if __name__ == "__main__":
  while(True):
    show_menu(db)