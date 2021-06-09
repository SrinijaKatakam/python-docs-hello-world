from flask import Flask, render_template
from datetime import datetime
import re
from azure.storage.blob import BlobServiceClient
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route("/page2")
def page2():
    return render_template('page2.html')



