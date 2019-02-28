#Wyatt Humphreys | wlhumphreys@student.rtc.edu
#Sources: https://stackoverflow.com/questions/8211128/multiple-distinct-pages-in-one-html-file
#https://stackoverflow.com/questions/902408/how-to-use-variables-in-sql-statement-in-python
#https://stackoverflow.com/questions/1081750/python-update-multiple-columns-with-python-variables
import mysql.connector
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, static_url_path='')


conn = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='zipcodedb',
                               buffered = True)
cursor = conn.cursor()
testcall = input("Enter a zipcode ")
testcall= int(testcall)
cursor.execute("SELECT * FROM `table 1` WHERE Zipcode='%s'", [testcall])
testprint = cursor.fetchall()
print(testprint)
testupdate = input("Enter a new Population")
testupdate = str(testupdate)
cursor.execute("UPDATE `table 1` SET EstimatedPopulation=%s WHERE Zipcode=%s", (testupdate, testcall))

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/search',methods = ['POST', 'GET'])
def search():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


@app.route('/update',methods = ['POST', 'GET'])
def update():
   print("some code goes here")

@app.route('/')
def root():
   return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)