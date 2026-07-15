from flask import Flask, request, render_template_string
import mysql.connector
import time
import os

app = Flask(__name__)

# HTML Page
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>School Bus Address Change</title>
</head>
<body>

<h2>School Bus Address Change Request</h2>

<form action="/submit" method="POST">

Student Name:<br>
<input type="text" name="student"><br><br>

Roll Number:<br>
<input type="text" name="roll"><br><br>

Current Address:<br>
<textarea name="old"></textarea><br><br>

New Address:<br>
<textarea name="new"></textarea><br><br>

<input type="submit" value="Submit">

</form>

</body>
</html>
"""

# Home page
@app.route("/")
def home():
    return render_template_string(HTML)

# Database connection
def connect_db():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DATABASE")
            )
            return conn
        except:
            print("Waiting for MySQL...")
            time.sleep(5)

# Submit form
@app.route("/submit", methods=["POST"])
def submit():
    student = request.form["student"]
    roll = request.form["roll"]
    old = request.form["old"]
    new = request.form["new"]

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO address_requests
        (student_name, roll_no, old_address, new_address)
        VALUES (%s, %s, %s, %s)
        """,
        (student, roll, old, new)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return f"""
    <h2 style='color:green;'>Address Change Request Submitted Successfully!</h2>
    <hr>
    <b>Student:</b> {student}<br><br>
    <b>Roll No:</b> {roll}<br><br>
    <b>Old Address:</b> {old}<br><br>
    <b>New Address:</b> {new}<br><br>
    <h3>Your request has been forwarded to the School Transport Department.</h3>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)