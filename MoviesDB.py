# Importing Packages
import sqlite3
import pandas as pd
# Creating DB using SQLiteJDBC driver
db = sqlite3.connect('../DB/_movies.db')
# DB Cursor
cursor = db.cursor()
# Creating Tables
# cursor.execute('''CREATE TABLE movies(id INTEGER PRIMARY KEY, Movie_Name TEXT, Lead_Actor TEXT, Lead_Actress TEXT, Director_Name TEXT, Year_Of_Release YEAR)''')
# Inserting Data into tables
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(1,"Ante Sundariniki","Nani","Nazriya","Vivek Athreya",2022)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(2,"Soorarai Potru","Surya","Aparna Balamurali","Sudha Kongara",2020)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(3,"Jugjugg Jeeyo","Varun Dhawan","Kiara Advani","Raj Mehta",2022)''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(4,"Life in a year","Jaden Smith,"Cara Delivgne","Mitja Okorn",2020)''')

# SELECT statement to query all rows from the Movies table
sqlite_select_query = """SELECT * from movies"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print(pd.DataFrame(records,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Director_Name","Year_Of_Release"]))

# SELECT query with parameter to select movies based on the year of release after 2019
sqlite_select_query = """SELECT * from movies where Year_Of_Release >2019"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print(pd.DataFrame(records,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Director_Name","Year_Of_Release"]))
