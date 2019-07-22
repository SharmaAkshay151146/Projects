from tkinter import *
from tkinter import ttk 
from students import *
import sqlite3

conn = sqlite3.connect('studnets2.db')
c = conn.cursor()
'''
c.execute(""" CREATE TABLE students (
				id integer,
				first text,
				last text,
				year integer)""")
'''

def insert_stud(stud):
	with conn:
		c.execute("INSERT INTO students VALUES (:id, :first, :last, :year)",
			{'id':stud.id, 'first':stud.first, 'last':stud.last, 'year':stud.year})

def get_stud_by_name(lastname):
	try:
		c.execute("SELECT * FROM students WHERE last=:last",{'last':lastname})
		return c.fetchall()
	except sqlite3.OperationalError:
		print("Table doesn't exist")
	except:
		print("Some other error occured during query by name")

def get_stud_by_id(id):
	try:
		c.execute("SELECT * FROM students WHERE id=:id",{'id':id})
		return c.fetchall()
	except sqlite3.OperationalError:
		print("Table doesn't exist")
	except:
		print("Some other error occured during query by id")

def update_year(first, last, year):
	try:
		c.execute("""UPDATE students SET year=:year WHERE first=:first AND last=:last""", {'first':first,'last':last,'year':year})
		c.commit()
	except sqlite3.OperationalError:
		print("Error occured during update.")
	except:
		print("Some other error occured during update")

def remove_stud_by_name(first, last):
	try:
		c.execute("DELETE from students WHERE first=:first AND last=:last",
			{'first':stud.first, 'last':stud.last})
		c.commit()
	except sqlite3.OperationalError:
		print("Error occured during removal.")
	except:
		print("Some other error occured during removal by name")

def remove_stud_by_id(stud):
	try:
		c.execute("DELETE from students WHERE id=:id", {'id':stud.id})
		c.commit()
	except sqlite3.OperationalError:
		print("Error occured during removal by id")
	except:
		print("Some other error occured during removal by id")

def get_all():
	try:
		c.execute('SELECT * FROM students')
		return c.fetchall()
	except sqlite3.OperationalError:
		print("Table doesn't exist")
	except:
		print("Some other error occured during getting all entries")

'''
stud_1 = Students(40,'Harry', 'Potter', 1)
stud_2 = Students(11,'Albus', 'Dumbeldore', 4)
stud_3 = Students(41,'Hermoine', 'Granger', 1)
stud_4 = Students(75,'Ronald', 'Weasley', 1)
stud_5 = Students(33,'Draco', 'Malfoy', 1)



insert_stud(stud_1)
insert_stud(stud_2)
insert_stud(stud_3)
insert_stud(stud_4)
insert_stud(stud_5)
'''

student = get_stud_by_id(40)
print(student)

student = get_stud_by_name('Malfoy')
print(student)

students = get_all()
print(students)

update_year('Albus', 'Dumbeldore',5)

students = get_all()
print(students)

conn.close()