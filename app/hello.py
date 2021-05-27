from flask import Flask, redirect, url_for, render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorschoose'
COLLECTION_NAME = 'projects'
FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}


@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/Programmer1')
def Programmer1():
    return render_template('Programmer1.html')
    
@app.route('/Programmer2')
def Programmer2():
    return render_template('Programmer2.html')
    
@app.route('/Programmer3')
def Programmer3():
    return render_template('Programmer3.html')
    
@app.route('/Programmer4')
def Programmer4():
    return render_template('Programmer4.html')
    
@app.route('/Programmer5')
def Programmer5():
    return render_template('Programmer5.html')

@app.route("/donorschoose/projects")
def donorschoose_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=50000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

if __name__ == '__main__':
    app.run(port = 5001,debug=True)

