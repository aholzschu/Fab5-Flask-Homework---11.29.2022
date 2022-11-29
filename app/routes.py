from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/sports')
@app.route('/home')
def sports():
    teams = ['1. Steve Nash - Pheonix Suns', '2. Joe Thomas - Cleveland Browns', '3. Brian Urlacher - Chicago Bears', '4. Michael Jordan - Chicago Bulls', '5. Pablo Sanchez - Backyard Baseball']
    return render_template('sports.html', favorites=teams)
