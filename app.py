from flask import render_template, Flask
import mysql.connector
from settings import db_server, db_user, db_passwd, db_name

def get_data():
    ###### SQL CONNECTION ######
    connection = mysql.connector.connect(
                                host=db_server,
                                database=db_name,
                                user=db_user,
                                password=db_passwd)

    cursor = connection.cursor()    
    query = ("SELECT * FROM yt_events ORDER BY id DESC")
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data

def get_events():
    ###### SQL CONNECTION ######
    connection = mysql.connector.connect(
                                host=db_server,
                                database=db_name,
                                user=db_user,
                                password=db_passwd)

    cursor = connection.cursor()
    query = ("SELECT * FROM yt_events WHERE YT_Tag = 'EVENT' ORDER BY id DESC")
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data

def get_thoughts():
    ###### SQL CONNECTION ######
    connection = mysql.connector.connect(
                                host=db_server,
                                database=db_name,
                                user=db_user,
                                password=db_passwd)

    cursor = connection.cursor()
    query = ("SELECT * FROM yt_events WHERE YT_Tag = 'THOUGHT' ORDER BY id DESC")
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data

def get_requests():
    ###### SQL CONNECTION ######
    connection = mysql.connector.connect(
                                host=db_server,
                                database=db_name,
                                user=db_user,
                                password=db_passwd)

    cursor = connection.cursor()
    query = ("SELECT * FROM yt_events WHERE YT_Tag = 'REQUEST' ORDER BY id DESC")
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data

###### FLASK SERVER ######
title = "REAPR Web - Tagged LiveStream Events"
headings = ("ID", "Tag", "Date/Time", "User", "Message")

app = Flask(__name__, template_folder="template")
@app.route('/')    
def index(): 
    data = get_data()
    return render_template("table.html", headings=headings, data=data, title=title)

    if (__name__ == '__main__'):
        app.run(debug=False)

@app.route('/events/')
def events():
    data = get_events()
    return render_template("table.html", headings=headings, data=data, title=title)

    if (__name__ == '__main__'):
        app.run(debug=False)

@app.route('/thoughts/')
def thoughts():
    data = get_thoughts()
    return render_template("table.html", headings=headings, data=data, title=title)

    if (__name__ == '__main__'):
        app.run(debug=False)

@app.route('/requests/')
def requests():
    data = get_requests()
    return render_template("table.html", headings=headings, data=data, title=title)

    if (__name__ == '__main__'):
        app.run(debug=False)

@app.route('/export/', methods=['GET'])
def export():
    si = StringIO()
    cw = csv.writer(si)
    rows = get_data()
    cw.writerow([heading[0] for heading in headings])
    cw.writerows(rows)
    response = make_response(si.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=REAPR-report.csv'
    response.headers["Content-type"] = "text/csv"
    return response
