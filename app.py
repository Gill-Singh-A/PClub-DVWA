#! /usr/bin/env python3

import os
from flask import Flask, render_template, request

app = Flask(__name__)
host = "127.0.0.1"
port = 7000
debug = True

@app.route("/gallery", methods=["GET"])
def index():
    image_files = os.listdir("static/images/gallery")
    image_data = []
    for image_file in image_files:
        image_data.append({"src": f"/static/images/gallery/{image_file}"})
    return render_template("gallery.html", images=image_data)

if __name__ == "__main__":
    app.run(host=host, port=port, debug=debug)