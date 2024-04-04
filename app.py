from flask import flash,Flask,render_template,redirect,url_for,jsonify,request,session
from flask_mysqldb import MySQL
from flask_session import Session
from py_mail import mail_sender
from datetime import datetime
from datetime import date
app=Flask(__name__)
app.secret_key='AG&SG'
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']='appu'
app.config['MYSQL_DB']='SAM'
app.config["SESSION_TYPE"] = "filesystem"
mysql=MySQL(app)
Session(app)

@app.route('/')
def welcome():
    return render_template('title.html')
@app.route('/create',methods=['GET','POST'])
def create():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT COUNT(*) from admin')
    count=cursor.fetchone()[0]
    cursor.close()
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        passcode=request.form['passcode']
        cursor=mysql.connection.cursor()
        cursor.execute('insert into admin values(%s,%s,%s,%s)',[name,email,passcode,password])
        mysql.connection.commit()
        flash('Details Registered Successfully')
        return redirect(url_for('adminlogin'))
    return render_template('signup.html')
@app.route('/adminlogin',methods=['GET','POST'])
def adminlogin():
    if session.get('email'):
        return redirect(url_for('fachome1'))
    if request.method=='POST':
        user=request.form['user']
        password=request.form['password']
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT EMAIL from admin where email=%s',[user])
        email=cursor.fetchone()[0]
        print(email)
        cursor.execute('select password from admin where email=%s',[user])
        user_password=cursor.fetchone()[0]
        cursor.execute('select passcode from admin where email=%s',[user])
        passcode=cursor.fetchone()[0]
        cursor.close()
        if email==user:
            if password==user_password:
                session['email']=user
                session['passcode']=passcode
                return redirect(url_for('fachome1'))
            else:
                flash('Invalid Password')
                render_template('adminlogin.html')
        else:
            flash('Invalid User Id')
            render_template('adminlogin.html')

    return render_template('adminlogin.html')

@app.route('/sturegistration',methods=['GET','POST'])
def studentform():
    if session.get('email'):
        if session.get('passcode'):
            if request.method=='POST':
                id1=request.form['Id']
                name=request.form['Name']
                gender=request.form['gender']
                phone=request.form['phone']
                mail=request.form['mail']
                password=request.form['password']
                Address=request.form['Address']
                dept=request.form['dept']
                #pay=request.form['attendence']
                cursor=mysql.connection.cursor()
                cursor.execute('select Target from work where added_by=%s',[session.get('email')])
                target=cursor.fetchone()
                #cursor.execute('insert ignore into student values(%s,%s,%s,%s,%s,%s,%s,%s)',[id1,name,gender,phone,mail,password,Address,dept])
                cursor.execute('insert  into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[id1,name,gender,phone,mail,password,Address,dept,target,session.get('email')])
                mysql.connection.commit()
                '''from_mail=session['email']
                passcode=session['passcode']
                subject=f'{name}, Your details are successfully with us!'
                url_path=request.host_url+url_for('adminlogin')
                body=f'Your user is {id1} and password is {password}\n\nYOU can login to the Student Attendence Management system with these details by going through\n\n\n {url_path} '
                try:
                    mail_sender(from_mail,mail,subject,body,passcode)
                except Exception as e:
                    print(e)
                    flash('There is trouble sending email confirmation\n check the sender mail but')'''
                flash('Details Registered Successfully')
            return render_template('registerpage.html')
    return redirect(url_for('adminlogin'))
@app.route('/login',methods=['GET','POST'])
def login():
    if session.get('user'):
        return redirect(url_for('fachome'))
    if request.method=='POST':
        user=request.form['user']
        password=request.form['password']
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT id from student')
        data=cursor.fetchall()
        cursor.execute('SELECT PASSWORD from student WHERE id=%s',[user])
        password_user=cursor.fetchone()
        cursor.close()
        if (int(user),) in data:
            if password==password_user[0]:
                session['user']=user
                return redirect(url_for('fachome'))
            else:
                flash('Invalid password')
                return render_template('login.html')
        else:
            flash('Invalid user Id')
            return render_template('login.html')
    return render_template('login.html')
@app.route('/fachome')
def fachome():
    if session.get('user'):
        return render_template('facultypage.html')
    return redirect(url_for('login'))
@app.route('/workdays',methods=['GET','POST'])
def workdays():
    if session.get('email'):
        if request.method=='POST':
            Target=request.form['Target']
            cursor=mysql.connection.cursor() 
            cursor.execute('insert into work(Target,added_by) values(%s,%s)',[Target,session.get('email')])
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('fachome1'))
        return render_template('workdays.html')
    return render_template('adminlogin.html')
@app.route('/studentcheckin')
def stu():
    if session.get('user'):
        today=date.today()
        day=today.day
        month=today.month
        year=today.year
        today_date=datetime.strptime(f'{year}-{month}-{day}','%Y-%m-%d')
        date_today=datetime.strftime(today_date,'%Y-%m-%d')
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT COUNT(*) FROM RECORDS WHERE DATE=%s AND id=%s',[date_today,session.get('user')])
        count=cursor.fetchone()[0]
        cursor.execute('select target from student where id=%s',[session.get('user')])
        target=cursor.fetchone()[0]
        cursor.execute("select COUNT(*) AS days from records group by ID")
        count1=cursor.fetchall()
        cursor.execute('select * from records where id=%s',[session.get('user')])
        data=cursor.fetchall()
        cursor.close()
        if count==0:
            cursor=mysql.connection.cursor()
            cursor.execute('select target from student where id=%s',[session.get('user')])
            target=cursor.fetchone()[0]
            cursor.execute('select name from student where id=%s',[session.get('user')])
            name=cursor.fetchone()[0]
            cursor.execute('insert into records(date,id,name,target) values(%s,%s,%s,%s)',[date_today,session.get('user'),name,target])
            mysql.connection.commit()
            cursor.execute('select * from records where id=%s',[session.get('user')])
            data=cursor.fetchall()
            cursor.close()
            return render_template('table.html',data=data)
        return render_template('table.html',data=data)
    return redirect(url_for('login'))
@app.route('/checkoutupdate/<date>/<id1>')
def checkoutupdate(id1,date):
    cursor=mysql.connection.cursor()
    cursor.execute('update records set checkout=current_timestamp() where Id=%s and date=%s',[id1,date])
    mysql.connection.commit()
    return redirect(url_for('stu'))
@app.route('/checkinupdate/<date>/<id1>')
def checkinupdate(id1,date):
    cursor=mysql.connection.cursor()
    cursor.execute('update records set checkin=current_timestamp() where Id=%s and date=%s',[id1,date])
    mysql.connection.commit()
    return redirect(url_for('stu'))
@app.route('/attpresent')
def student_presentage():
    if session.get('user'):
        cursor=mysql.connection.cursor()
        cursor.execute("select id,date_format(date,'%M %Y') as Month,COUNT(*) AS DAYS from records group by ID,MONTH ORDER BY MONTH")
        data=cursor.fetchall()
        cursor.execute('select target from student where id=%s',[session.get('user')])
        target=cursor.fetchone()[0]
       
        cursor.execute('select COUNT(*) AS days from records  where id=%s',[session.get('user')])
        count1=cursor.fetchall()
        print(count1)
        a=list(count1)
        b=[i for x in a for i in x]
        c=b.count(1)
        presentage=(c/target)*100
        cursor.close()
        return render_template('months.html',data=data,presentage=presentage)
      
    return redirect(url_for('login'))
@app.route('/attpresent1')
def total_presentage():
    if session.get('email'):
        cursor=mysql.connection.cursor()
        cursor.execute("select id,date_format(date,'%M %Y') as Month,COUNT(*) AS DAYS from records group by ID,MONTH ORDER BY MONTH")
        data=cursor.fetchall()
        
        return render_template('month1.html',data=data)
    return redirect(url_for('adminlogin'))
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('welcome'))
@app.route('/adminlogout')
def alogout():
    session.pop('email')
    return redirect(url_for('welcome'))
@app.route('/sturecords')
def records():
    cursor=mysql.connection.cursor()
    cursor.execute('select * from records order by date')
    data=cursor.fetchall()
    cursor.close()
    return render_template('status.html',data=data)
@app.route('/fachome1')
def fachome1():
    if session.get('email'):
        return render_template('homepage.html')
    return redirect(url_for('adminlogin'))
app.run(use_reloader=True,debug=True)