from flask import Flask
from flask import render_template
from flask import request
from flask import session
from bs4 import BeautifulSoup
import sqlite3
import requests
import json
import pafy

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
    filename = best.download(filepath = './')

    return 'test'

if __name__ == '__main__' :
    app.debug = True
    app.run()