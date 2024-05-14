#! /usr/bin/env python3

import os, json
from pathlib import Path
from hashlib import sha3_512, md5
from mysql.connector import connect, Error
from flask import Flask, render_template, request

app = Flask(__name__)
host = "127.0.0.1"
port = 2324
debug = True

with open("db_user.json", 'r') as file:
    login_details = json.load(file)
database = "pclub_secy_task"
blog_parts = {"title": 1, "content": 2, "link": 3}

not_allowed_files = ["app.py"]
cwd = Path.cwd()

@app.route("/", methods=["GET"])
def indexRoute():
    return render_template("index.html")
@app.route("/gallery", methods=["GET"])
def galleryRoute():
    image_files = os.listdir("static/images/gallery")
    image_data = []
    for image_file in image_files:
        image_data.append({"src": f"/getFile?file={str(cwd)}/static/images/gallery/{image_file}"})
    return render_template("gallery.html", images=image_data)
@app.route("/blogs", methods=["GET"])
def blogsRoute():
    return render_template("blogs.html")
@app.route("/secretary_login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        password = md5(request.form["password"].encode()).hexdigest()
        connection = connect(host="localhost", user=login_details["user"], password=login_details["password"])
        cursor = connection.cursor()
        cursor.execute(f"USE {database}")
        cursor.execute(f"SELECT password FROM USERS WHERE userhash='{sha3_512(user.encode()).hexdigest()}'")
        original_password = cursor.fetchall()
        cursor.close()
        connection.close()
        if len(original_password) == 1:
            original_password = original_password[0][0]
            if original_password == password:
                return render_template("login.html", message="User have not File or Data to Show!")
            else:
                return render_template("login.html", message="Incorrect Password")
        else:
            return render_template("login.html", message="User Not Found")
    return render_template("login.html")
@app.route("/recovery", methods=["GET"])
def recoveryRoute():
    return render_template("recovery.html")
@app.route("/robots.txt", methods=["GET"])
def robotsRoute():
    return render_template("robots.html")
@app.route("/getFile", methods=["GET"])
def getFileRoute():
    file_name = request.args.get("file")
    for file in not_allowed_files:
        if file in file_name:
            return "Not Allowed", 403
    with open(file_name, 'rb') as file:
        content = file.read()
    return content, 200
@app.route("/getBlogDetail", methods=["GET"])
def getBlogDetailRoute():
    blog_index = request.args.get("blog")
    blog_part = request.args.get("part")
    connection = connect(host="localhost", user=login_details["user"], password=login_details["password"])
    cursor = connection.cursor()
    cursor.execute(f"USE {database}")
    cursor.execute(f"SELECT * FROM BLOGS WHERE id='{blog_index}'")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    result = result[0][blog_parts[blog_part]]
    return result

if __name__ == "__main__":
    app.run(host=host, port=port, debug=debug)