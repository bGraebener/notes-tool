import json
from flask import Flask
from flask_pymongo import PyMongo
from flask import request
from flask import jsonify
from bson import ObjectId
# from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)

# ***************** REST ***********************
@app.route('/notes', methods=['GET'])
def get_all_notes():
    notes = mongo.db.notes
    output = []
    for note in notes.find():
        output.append(Note(note= note['note'], description= note['description'], tags= note['tags'], dateTime= note['dateTime']))
    response = jsonify(output)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/notes/', methods=['GET'])
def get_notes_by_tag(tag):
    notes = mongo.db.notes


@app.route('/notes', methods=['POST'])
def add_a_note():
    notesDB= mongo.db.notes
    jsonResponse = request.json
    print(jsonResponse)
    note = Note(note=jsonResponse['note'], description=jsonResponse['description'], tags=jsonResponse['tags'], dateTime=datetime.today().isoformat())
    noteID = notesDB.insert_one(note.__dict__)

    #return json.dumps(note, default=json_encoder, indent=4)
    return jsonify(note = note)


# ****************** Class *********************
class Note():
    def __init__(self, note, description, tags, dateTime):
        self.note = note
        self.description = description
        self.tags = tags
        self.dateTime = dateTime

    def __str__(self):
        return """
        {} -- {}
        {}
        {}""".format(self.dateTime, self.tags, self.note, self.description)

class NoteEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Note):
            return obj.__dict__
        elif isinstance(obj, ObjectId):
            return str(obj)
        else:
            return super(NoteEncoder, self).default(obj)

# ***************** JSON ***********************
def json_encoder(obj):
    if isinstance(obj, ObjectId):
        return str(obj)

    return obj.__dict__


app.json_encoder = NoteEncoder
# CORS(app)
MONGODB_USER = os.environ['MONGODB_USER']
MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD']
MONGODB_DATABASE = os.environ['MONGODB_DATABASE']
print(MONGODB_USER)

app.config["MONGO_URI"] = "mongodb://{}:{}@{}".format(MONGODB_USER, MONGODB_PASSWORD,MONGODB_DATABASE)
mongo = PyMongo(app)

if __name__ == '__main__':
    app.run(debug=True)