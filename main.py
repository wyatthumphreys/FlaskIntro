#Wyatt Humphreys | wlhumphreys@student.rtc.edu
#Sources: https://stackoverflow.com/questions/8211128/multiple-distinct-pages-in-one-html-file
#https://stackoverflow.com/questions/902408/how-to-use-variables-in-sql-statement-in-python
#https://stackoverflow.com/questions/1081750/python-update-multiple-columns-with-python-variables
#https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for
#https://github.com/vimalloc/flask-jwt-extended/issues/175
import mysql.connector
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, static_url_path='')


conn = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='zipcodedb',
                               buffered = True)
cursor = conn.cursor()
#testcall = input("Enter a zipcode ")
#testcall= int(testcall)
#cursor.execute("SELECT * FROM `table 1` WHERE Zipcode='%s'", [testcall])
#testprint = cursor.fetchall()
#print(testprint)
#testupdate = input("Enter a new Population ")
#testupdate = str(testupdate)
#cursor.execute("UPDATE `table 1` SET EstimatedPopulation=%s WHERE Zipcode=%s", (testupdate, testcall))

@app.route('/success/<name>')
def success(name):
    cursor.execute("SELECT * FROM `table 1` WHERE Zipcode=%s", [name])
    name = cursor.fetchall()
    return '%s' % name

@app.route('/nowupdate/<name> <name2>')
def nowupdate(name, name2):
    cursor.execute("UPDATE `table 1` SET EstimatedPopulation=%s WHERE Zipcode=%s", (name2, name))
    return 'success'

@app.route('/search',methods = ['POST', 'GET'])
def search():
    user = request.form['nm']
    return redirect(url_for('success',name = user))


@app.route('/update',methods = ['POST', 'GET'])
def update():
    user = request.form['zip']
    user2 = request.form['pop']
    return redirect(url_for('nowupdate', name=user, name2=user2))

@app.route('/')
def root():
   return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)