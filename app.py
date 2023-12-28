import os
import csv
import threading
from config import Config
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Oprations.csvscraper import CSV_Scraper 

app = Flask(__name__)
csvsr = CSV_Scraper()

def hello(a):
    return a

@app.route('/')
def index():
    loop_limit=101
    thread = threading.Thread(target=hello, args=(2,))
    thread.start()
    return "CSV scraping started. Check your console for updates."


if __name__ == "__main__":
    app.run(debug=True)
