from flask import Flask, request, jsonify, render_template
import json
import webbrowser 
import threading
import pymysql
import os
from dotenv import load_dotenv
from decouple import config
from decryption import *

prds = []

price = 0

namea = []

global sl

sl = 0



mat1=[44, 116, 111, 106, 105, 183, 155, 121, 157, 140]
mat2=[9,2,4,6,7,74,34,6,44,32]

val = dcr(mat1,mat2)

def con():
	
	return pymysql.connect(
		
		host = f"mysql://root:{val}@Ravikiran:3306/ravi_stores",
		user = os.getenv("DB_USER"),
		password = val,
		database = os.getenv("DB_DATABASE"),
		port = int(os.getenv("DB_PORT", 3306))
		
	)
	
def crt():
	
	conn = con()
	
	cursor = conn.cursor()
	
	cursor.execute('''
	
		create table if not exists rs_data (
			
			Slno int auto_increment primary key,
			Name varchar(100),
			Ph_number bigint, 
			Price int, 
			Items varchar(300)
			
		);
	''')
	
	conn.commit()
	conn.close()
		
def add(nme,phn,prc,its):
	
	conn = con()
	
	cursor = conn.cursor()
	
	cursor.execute('''
		insert into rs_data (Name,Ph_number,Price,Items)values( %s, %s, %s, %s)
	''',(nme,phn,prc,json.dumps(its)))
	
	conn.commit()
	conn.close()

def view():
	
	conn = con()
	
	cursor = conn.cursor()
	
	cursor.execute("select * from rs_data")
	
	data = cursor.fetchall()
	
	conn.close()
	
	return data
	

load_dotenv()

app = Flask(__name__)

crt()

if len(view())>0:
	
	j = list(view())

	k = j[len(j)-1]

	sl = k[0]+1
else:
	sl = 1

@app.route('/')
def check():
	
	return render_template("htmlpy.html",sln=sl)

@app.route('/icn')
def icon():
	
	return app.send_static_file('icon.png')

def open_browser():
    webbrowser.open("http://localhost:5000")


@app.route('/api/bill',methods=['GET'])
def chk():
	
	val = jsonify(view())
	
	return val

@app.route('/view')
def call():
	
	return render_template("htmlpy2.html")


@app.route('/api/bill',methods=['POST'])
def bill():
		
	data = request.get_json()
		
	sln = data.get('slno')
	name = data.get('Customer')
	namea.append(data.get('Customer'))
	phone = data.get('Phone')
	products = data.get('Products')
		
	process(products)
		
	add(name,phone,price,prds)
	
	#view_data()
		
	return jsonify({'Sl.No.':f'{sln}','Name':f'{name}','Phone':f'{phone}','Products':f'{products}'})
		


def process(products):
	
	lst = products
	
	global prds
	
	global price
	
	price = 0
	
	prds = []
	
	secondary = 0
	
	restrict = 0
	restrict1 = 0
	
	for i in lst:
		
		if restrict==0:
			
			prds.append(i)
		
		if restrict>0:
			
			if restrict1==0:
				
				sec = int(i)
				
				if restrict1==1:
					restrict1=0
				else:
					restrict1+=1
				
			elif restrict1==1:
				
				price += sec * int(i)
				
				if restrict1==1:
					restrict1=0
				else:
					restrict1+=1
		
		if restrict==2:
			
			restrict = 0
		else:
			restrict+=1


@app.route('/price',methods=['GET'])
def price():
		
	return render_template('price.html',name=namea[0],pric=price,pro=prds)


if __name__ == '__main__':
	
	#threading.Timer(0, open_browser).start()
	
	open_browser()
	
	app.run(debug=True)
