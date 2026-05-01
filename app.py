from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    address = request.form['address']
    description = request.form['description']

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Himanshu4444@',
        database='form'
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO freelancer (name, email, mobile, address, description) VALUES (%s, %s, %s, %s, %s)", (name, email, mobile, address, description))
    conn.commit()
    conn.close()

    return "Data Save Ho Gaya! ✅"

if __name__ == '__main__':
    app.run(debug=True)