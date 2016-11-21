from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import send_file
from flask import Response, stream_with_context
from flask import redirect
from bs4 import BeautifulSoup
from subprocess import call
import StringIO
import socket
import sqlite3
import requests
import json
import pafy
import urllib
import os
import io

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("app.html")

@app.route('/ytube', methods = ['GET'])
def get_file():

    url = request.args.get('ysearch')

    #json_file = json.loads(requests.get(url).text)
    #html_file = BeautifulSoup(requests.get(url).text)

    video = pafy.new(url)
    best = video.getbest()

    filename = best.download()

    print(filename)

    #sound = AudioSegment.from_file(filename)

    f = open(filename, "r")
    sound_data = f.read()
    strIO = StringIO.StringIO()
    strIO.write(sound_data)
    strIO.seek(0)
    os.remove(filename)

    #return redirect(best.url)
    return send_file(strIO, attachment_filename = filename.encode('utf-8'), as_attachment=True)
    #return Response(stream_with_context(sound_data))
    return 'test'

if __name__ == '__main__' :
    app.debug = True
    app.run(host='0.0.0.0')