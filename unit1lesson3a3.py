# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 21:53:47 2015

@author: Mark
"""

import pandas as pd
import sqlite3 as lite
con=lite.connect("E:\Users\Mark\getting_started.db")

cityname=raw_input("Enter a city name to see whether its warmest month is July: ")

with con:
	cur=con.cursor()
	cur.execute("drop table if exists cities;")
	cur.execute("drop table if exists weather;")
	cur.execute("create table cities (name text, state text);")
	cur.execute("create table weather ('city' text, 'year' integer, 'warm_month' text, 'cold_month' text, 'average_high' integer);")
	
	cities_tuple=(('New York City','NY'),('Boston', 'MA'),('Chicago', 'IL'),('Miami', 'FL'),('Dallas', 'TX'),('Seattle', 'WA'),('Portland', 'OR'),('San Francisco', 'CA'),('Los Angeles', 'CA'))

	cur.executemany("insert into cities values (?,?)",cities_tuple)

	weather_tuple=(('New York City',2013,'July','January',62),
			      ('Boston',2013,'July','January',59),
			      ('Chicago',2013,'July','January',59),
			      ('Miami',2013,'August','January',84),
			      ('Dallas',2013,'July','January',77),
			      ('Seattle',2013,'July','January',61),
			      ('Portland',2013,'July','December',63),
			      ('San Francisco',2013,'September','December',64),
			      ('Los Angeles',2013,'September','December',75))

	cur.executemany("insert into weather values(?,?,?,?,?)", weather_tuple)

	cur.execute("select * from cities c, weather w where c.name=w.city;")
	rows=cur.fetchall()

cols=[desc[0] for desc in cur.description]
df=pd.DataFrame(rows, columns=cols)

found_city=False

for a in df.iterrows():
    if a[1][0]==cityname and a[1][4]=='July':
        print "The hottest month in",cityname, "is July, with an average temp of", a[1][6]
        found_city=True        
        break

if found_city == False:
    print "Your city's warmest month is not July :("