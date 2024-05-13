#! /usr/bin/env python3

import os
from flask import Flask, render_template, request

app = Flask(__name__)
hosted_url = "127.0.0.1"
host = "127.0.0.1"
port = 7000
debug = True

not_allowed_files = ["app.py"]

@app.route("/gallery", methods=["GET"])
def galleryRoute():
    image_files = os.listdir("static/images/gallery")
    image_data = []
    for image_file in image_files:
        image_data.append({"src": f"http://{hosted_url}:7000/getFile?file=/home/kaptaan/IIT_Kanpur/Clubs/PClub/Secretary-Recruitment/2023-24/PClub-DVWA/static/images/gallery/{image_file}"})
    return render_template("gallery.html", images=image_data)
@app.route("/getFile", methods=["GET"])
def getFileRoute():
    file_name = request.args.get("file")
    for file in not_allowed_files:
        if file in file_name:
            return "Not Allowed", 403
    with open(file_name, 'rb') as file:
        content = file.read()
    return content, 200

if __name__ == "__main__":
    app.run(host=host, port=port, debug=debug)