import mysql.connector, time
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, static_url_path='')


conn = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='zipcodedb',
                               buffered = True)
cursor = conn.cursor()
cursor.execute("SELECT * FROM `table 1` WHERE Zipcode=98056;")
testfetch = cursor.fetchall()
print(testfetch)

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