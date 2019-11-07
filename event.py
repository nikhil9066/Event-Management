from flask import Flask
from flask import render_template,redirect,request,url_for
from flask import request
import firebase_admin
from firebase_admin import credentials,db,auth
import socket  
import os 
import smtplib
import webbrowser
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('intro.html')

@app.route('/sendmessage',methods=["GET", "POST"])
def sendmessage():
	if request.method == 'GET':
		fromname = request.values.get('Name')
		emailid = request.values.get('Email')
		message = request.values.get('Message')
		s=smtplib.SMTP('smtp.gmail.com:587')
		s.ehlo()
		s.starttls()
		s.login('eventmanagerishere@gmail.com','eventmanager@123')
		message='Subject:Message from '+fromname+'\n\n'+message
		s.sendmail('eventmanagerishere@gmail.com','eventmanagerishere@gmail.com',message)
		s.quit()
		return render_template('intro.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/accordino')
def accordino():
	return render_template('accordino.html')

@app.route('/logout')
def logout():
	return render_template('logoutbut.html')

@app.route('/convention')
def convention():
	ref = db.reference('/conventions')
	conventions=ref.get()
	conventions['cnv05']['Block']='FLASH'
	return render_template('convention.html',conventions=conventions)

@app.route('/photo')
def photo():
	ref = db.reference('/photographers')
	photographers=ref.get()
	return render_template('index.html',photographers=photographers)

@app.route('/single/<pid>')
def single(pid):
	ref = db.reference('/photographers/'+pid)
	photographer=ref.get()
	return render_template('single.html',pid=pid,photographer=photographer)

@app.route('/services/<pid>')
def services(pid):
	ref = db.reference('/photographers/'+pid)
	photographer=ref.get()
	return render_template('services.html',pid=pid,photographer=photographer)

@app.route('/chatra/<cid>')
def chatra(cid):
	print(cid)
	ref = db.reference('/conventions/'+cid)
	convention=ref.get()
	return render_template('chatra.html',cid=cid,convention=convention)

@app.route('/music')
def music():
	ref = db.reference('/artists/')
	artists=ref.get()
	return render_template('music.html',artists=artists)

@app.route('/dress')
def dress():
	return render_template('dress.html')

@app.route('/product')
def product():
	return render_template('product.html')

@app.route('/artist/<aid>')
def artist(aid):
	ref = db.reference('/artists/'+aid)
	artist=ref.get()
	return render_template('artist.html',artist=artist,aid=aid)

@app.route('/musicload')
def musicload():
	return render_template('musicload.html')

@app.route('/caterers')
def caterers():
	ref = db.reference('/caterers/')
	caterers=ref.get()
	return render_template('caterers.html',caterers=caterers)

@app.route('/food/<cid>')
def food(cid):
	ref = db.reference('/caterers/'+cid)
	caterer=ref.get()
	return render_template('food.html',cid=cid,caterer=caterer)

@app.route('/form')
def form():
	return render_template('form.html')

@app.route('/introl')
def introl():
	return render_template('introl.html')

@app.route('/500')
def error500():
	return render_template('error500.html')

@app.route('/ud1')
def ud1():
	return render_template('ud1.html')

@app.route('/ud2')
def ud2():
	return render_template('ud2.html')

@app.route('/process/<uid>')
def process(uid):
	return render_template('process.html',uid=uid)

@app.route('/looading/<uid>')
def looading(uid):
	return render_template('looading.html',uid=uid)


@app.route('/payment')
def payment():
	return render_template('payment.html')

@app.route('/final')
def final():
	return render_template('final.html')

@app.route('/database')
def database():
	return render_template('database.html')

@app.route('/invitation/<uid>')
def invitation(uid):
	ref = db.reference('/')
	data=ref.get()
	email=(auth.get_user(uid).email)
	#mailing convention
	s=smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.login('eventmanagerishere@gmail.com','eventmanager@123')
	message='Subject:Booking Details from event manager\n\nMr. '+email+' has booked your Convention hall, '+data['conventions'][data['users'][uid]['convention']['cid']]['Name']+' on '+data['users'][uid]['date']
	s.sendmail('eventmanagerishere@gmail.com',data['conventions'][data['users'][uid]['convention']['cid']]['email'],message)
	s.quit()
	#mailing photographer
	s=smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.login('eventmanagerishere@gmail.com','eventmanager@123')
	message='Subject:Booking Details from event manager\n\nMr. '+email+' has booked services on '+data['users'][uid]['date']+' at '+data['conventions'][data['users'][uid]['convention']['cid']]['Name']+'.'
	s.sendmail('eventmanagerishere@gmail.com',data['photographers'][data['users'][uid]['photo']['pid']]['email'],message)
	s.quit()
	#mailing artist
	s=smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.login('eventmanagerishere@gmail.com','eventmanager@123')
	message='Subject:Booking Details from event manager\n\nMr. '+email+' has booked services on '+data['users'][uid]['date']+' at '+data['conventions'][data['users'][uid]['convention']['cid']]['Name']+'.'
	s.sendmail('eventmanagerishere@gmail.com',data['artists'][data['users'][uid]['music']['aid']]['email'],message)
	s.quit()
	#mailing caterer
	s=smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.login('eventmanagerishere@gmail.com','eventmanager@123')
	message='Subject:Booking Details from event manager\n\nMr. '+email+' has booked catering services on '+data['users'][uid]['date']+' at '+data['conventions'][data['users'][uid]['convention']['cid']]['Name']+'.'
	message+='\nBreakfast\n'
	for food in data['users'][uid]['food']['breakfast']:
		message+=(food+',')
	message+='\nLunch\n'
	for food in data['users'][uid]['food']['lunch']:
		message+=(food+',')
	message+='\nSnacks\n'
	for food in data['users'][uid]['food']['snacks']:
		message+=(food+',')
	message+=('\nExtra: '+data['users'][uid]['food']['extra'])
	message+=('\nQty: '+data['users'][uid]['peoplecount'])
	s.sendmail('eventmanagerishere@gmail.com',data['caterers'][data['users'][uid]['food']['cid']]['email'],message)
	s.quit()
	return render_template('invitation.html',data=data,uid=uid)

@app.route('/ack/<uid>')
def ack(uid):
	ref = db.reference('users/'+uid)
	data=ref.get()
	ref = db.reference('/')
	alldata=ref.get()
	return render_template('ack.html',uid=uid,data=data,alldata=alldata)

IPAddr = socket.gethostbyname(socket.gethostname() ) 
if __name__ == '__main__':
	print(" * Starting to connect to database")
	cred = credentials.Certificate('./cred.json')
	default_app = firebase_admin.initialize_app(cred,{
		'databaseURL': 'https://event-ab123.firebaseio.com/'
		})
	webbrowser.open_new('http://'+IPAddr+':5001')
	print(" * Database connected successfully")
	app.debug = True
	app.run(host=IPAddr,port=5001)