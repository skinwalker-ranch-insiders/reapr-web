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
