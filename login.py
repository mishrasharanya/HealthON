from csv import writer
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='Moulya@26',database='HealthON')
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS LIST_OF_USERS (email char(50),password char(50))')
def signup():
	emailid=input("EMAIL ID:")
	flag2=1
	while(flag2==1):
		pword=input("CREATE PASSWORD:")
		pword1=input("RE-ENTER PASSWORD:")
		if(pword==pword1):
			flag2=0
		else:
			print("Error! Passwords do not match")
	weight=float(input("WEIGHT(IN kg):"))
	height=float(input("HEIGHT(IN cm):"))
	bmi=weight/((height*height)/10000)
	query1='INSERT INTO LIST_OF_USERS(email, password) VALUES ("{}","{}")'.format(emailid,pword)
	cursor.execute(query1)
	conn.commit()
	cursor.execute('CREATE TABLE IF NOT EXISTS '+emailid+'(email char(50), password char(50), weight integer, height integer, bmi double)')
	query2='INSERT INTO '+emailid+'(email, password, weight, height, bmi) VALUES ("{}","{}",{},{},{})'.format(emailid,pword,weight,height,bmi)
	cursor.execute(query2)
	conn.commit()
	'''
	++MEASUREMENTS
	print("*****************")
	print("CHOOSE YOUR GOAL")
	print("*****************")
	print("1) WEIGHT LOSS")
	print("2) MUSCLE GAIN")
	'''
def login():
	flag=1
	while flag==1:
		emailid=input("EMAIL ID:")
		p=input("ENTER PASSWORD:")
		l=tuple([emailid,p])
		cursor.execute('select email,password from LIST_OF_USERS')
		myresult=cursor.fetchall()
		if l not in myresult:
			print("Email Id and password does not match/exist")
		else:
			print("LOGIN SUCCEESSFUL")
			flag=0

		
print("WELCOME TO HealthON")
print("already have an account: click 1 to login")
print("Create an account: click 2")
n=int(input())
if n==1:
	login()
elif n==2:
	signup()
else:
	print("Incorrect Choice")