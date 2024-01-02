from asyncio.windows_events import NULL
from multiprocessing import connection
from config import Config
from flask import Flask, render_template, request, redirect, url_for
from Oprations.csvscraper import CSV_Scraper 
from Oprations.db import Model
app = Flask(__name__)
cssscr=CSV_Scraper()
model=Model()
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/plannerdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
@app.route('/', methods=['GET', 'POST'])
def validate_titles():
    if request.method == 'POST':
        titles, number_of_rows = cssscr.scrape_titles(request)
        try:
            verticals=model.get_verticals()
                        
        except:
            return render_template('validate-datatype.html',message="Verticals List is not available")            
        if number_of_rows is None:
            return render_template('validate-datatype.html',message="Invalid Titles")
        return render_template('validate-datatype.html', headers=titles, row_count=number_of_rows,verticals=verticals)
    return render_template('validate-datatype.html')


if __name__ == "__main__":
    app.run(debug=True)
