# REAPR-web is a web front end providing access to reapr_db
# and the data collected with REAPR from the Skinwalker Ranch
# Insiders program.
#
# The intent is be able to log observations quickly from YT
# Chat and save them in a database for later review. To
# support reading, sorting, filtering and exporting this data
# REAPR-web was developed.
#
# Authored by: Robert Kris Davies <robert.kris.davies@hackshack.sh>
# Supported by: Skinwalker Ranch Insiders - Testing and Feedback
#               @Kris - We Have Fun : Insiders Discord - Consultant
#               @johns67467 : Insider Discord - Database Code Contribution
#               @John Neiberger : Insider Discord - Code Review
import csv
import mysql.connector
from settings import db_server, db_user, db_passwd, db_name
from flask import render_template, make_response, Flask
from io import StringIO


def load_all_from_db():
    """Retrieve all data from database"""
    connection = mysql.connector.connect(
        host=db_server, database=db_name, user=db_user, password=db_passwd
    )

    cursor = connection.cursor()
    query = "SELECT * FROM yt_events ORDER BY id DESC"
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data


def get_activity(activity_type):
    """Load specified activity type from database"""
    with mysql.connector.connect(
        host=db_server, database=db_name, user=db_user, password=db_passwd
    ) as connection:
        cursor = connection.cursor()
        query = (
            f"SELECT * FROM yt_events WHERE YT_Tag = '{activity_type}' ORDER BY id DESC"
        )
        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()
        return data


###### FLASK SERVER ######
title = "REAPR Web - Tagged LiveStream Events"
headings = ("ID", "Tag", "Date/Time", "User", "Message", "In SS")

app = Flask(__name__, template_folder="template")
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    data = load_all_from_db()
    return render_template("table.html", headings=headings, data=data, title=title)
    if __name__ == "__main__":
        app.run(debug=False)


@app.route("/events/")
def events():
    data = get_activity("EVENT")
    return render_template("table.html", headings=headings, data=data, title=title)
    if __name__ == "__main__":
        app.run(debug=False)


@app.route("/thoughts/")
def thoughts():
    data = get_activity("THOUGHT")
    return render_template("table.html", headings=headings, data=data, title=title)
    if __name__ == "__main__":
        app.run(debug=False)


@app.route("/requests/")
def requests():
    data = get_activity("REQUEST")
    return render_template("table.html", headings=headings, data=data, title=title)
    if __name__ == "__main__":
        app.run(debug=False)


@app.route("/feedback/")
def feedback():
    data = get_activity("FEEDBACK")
    return render_template("table.html", headings=headings, data=data, title=title)
    if __name__ == "__main__":
        app.run(debug=False)


@app.route("/export/", methods=["GET"])
def export():
    si = StringIO()
    cw = csv.writer(si)
    rows = load_all_from_db()
    cw.writerow([heading[0] for heading in headings])
    cw.writerows(rows)
    response = make_response(si.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=REAPR-report.csv"
    response.headers["Content-type"] = "text/csv"
    return response
    if __name__ == "__main__":
        app.run(debug=False)
