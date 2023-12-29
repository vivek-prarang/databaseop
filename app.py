from asyncio.windows_events import NULL
from multiprocessing import connection
from config import Config
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Oprations.csvscraper import CSV_Scraper 
from Oprations.db import Model as model

app = Flask(__name__)
cssscr=CSV_Scraper()



@app.route('/', methods=['GET', 'POST'])
def validate_titles():
    if request.method == 'POST':
        titles, number_of_rows = cssscr.scrape_titles(request)
        if number_of_rows is None:
            return render_template('validate-datatype.html',message="Invalid Titles")
        return render_template('validate-datatype.html', headers=titles, row_count=number_of_rows)
    return render_template('validate-datatype.html')

if __name__ == "__main__":
    app.run(debug=True)
