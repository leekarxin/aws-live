from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'customer'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddCus.html')


@app.route("/about", methods=['POST'])
def about():
    return render_template('www.citylinkexpress.com')


@app.route("/addemp", methods=['POST'])
def AddEmp():
    sname = request.form['sname']
    semail = request.form['semail']
    sphone = request.form['sphone']
    saddress = request.form['saddress']
    sitem = request.form['sitem']

    rname = request.form['rname']
    rphone = request.form['rphone']
    raddress = request.form['raddress']

    insert_sql = "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    try:

        cursor.execute(insert_sql, (sname, semail, sphone, saddress, sitem, rname, rphone, raddress))
        db_conn.commit()

        except Exception as e:
        return "Error occurred with message: " + str(e)
    finally:
        cursor.close()

    return render_template('success.html', sname=sname, sitem=sitem, rname=rname, raddress=raddress)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

