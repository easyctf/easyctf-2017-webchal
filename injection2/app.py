from flask import Flask, send_file, request, render_template
import pymysql

app = Flask(__name__, template_folder=".")


@app.route("/", methods=["GET", "POST"])
def index():
    logged_in = False
    connection = pymysql.connect(host="db",
                                 user="injection2",
                                 password="injection2",
                                 db="injection2",
                                 charset="utf8mb4",
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        error = ""
        if request.method == "POST":
            username = request.form.get("username", "")
            password = request.form.get("password", "")
            with connection.cursor() as cursor:
                cursor.execute('select * from `users` where username="%s" and password="%s"' % (username, password))
                result = cursor.fetchone()
                if result and result.get("username", "") == "leet1337":
                    try:
                        if int(result.get("power_level", "")) > 9000:
                            logged_in = True
                        else:
                            error = "Power level is not high enough!"
                    except:
                        error = "SQL Error: Wrong data type."
                else:
                    error = "Incorrect login."
    except:
        pass
    return render_template("index.html", logged_in=logged_in, error=error)

app.run(host="0.0.0.0", port=80)
