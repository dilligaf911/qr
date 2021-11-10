from app import app
from flask import render_template, request
import requests, json
import sqlite3 as sql

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from codes")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)


def create_content(filename):	
	return out["items"]

@app.route('/', methods=['GET', 'POST'])
def index():
	#if request.method == 'POST':
	#	str1 = request.form['name']
	#	return render_template('index.html', content=create_content("1"))
	#else:
	return render_template('index.html', userid='No data', bg='ff0')

@app.route('/qr/<uuid:userid>')
def check_qr(userid):
   con = sql.connect("database.db")
   con.row_factory = sql.Row   
   cur = con.cursor()
   cur.execute("select * from codes where uuid='" + str(userid) + "'")
   rows = cur.fetchall();

   if rows:
     name = rows[0]["name"]
     surname = rows[0]["surname"]
     photo = rows[0]["photo"]
     if rows[0]["valid"] == 0:
       message = "Code not valid!"
       return render_template('index.html', message=message, name=name, photo=photo, surname=surname, bg='f00')
     else:
       message = "Code is ok!"
       return render_template('index.html', message=message, name=name, photo=photo, surname=surname, bg='0f0')
   else:
     return render_template('wrong.html', name="UUID not found!", bg='f00')	   

