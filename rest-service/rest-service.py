import json
from flask import Flask
from flask_pymongo import PyMongo
from flask import request
from flask import jsonify
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/notes"
mongo = PyMongo(app)

# ***************** REST ***********************

@app.route('/notes', methods=['GET'])
def get_all_notes():
    notes = mongo.db.notes
    output = []
    for note in notes.find():
        output.append({'note': note['text'], 'description': note['description'], 'tags': note['tags'], 'date_time': note['date_time']})
    return jsonify({'result': output})


@app.route('/notes/', methods=['GET'])
def get_notes_by_tag(tag):
    notes = mongo.db.notes
    note = notes.findAll({'tags': tag})
    if note:
        output = {'note': note['note'], 'description': note['description'], 'date_time': note['date_time'] }

@app.route('/notes', methods=['POST'])
def add_a_note():
    notesDB= mongo.db.notes
    jsonResponse = request.json
    note = Note(note=jsonResponse['note'], description=jsonResponse['description'], tags=jsonResponse['tags'], date_time=jsonResponse['date_time'])
    noteID = notesDB.insert_one(note.__dict__)

    return json.dumps(note, default=convert_to_dict, indent=4)


# ****************** Class *********************
class Note(object):
    def __init__(self, note, description, tags, date_time):
        self.note = note
        self.description = description
        self.tags = tags
        self.date_time = date_time

    def __str__(self):
        return """
        {} -- {}
        {}
        {}""".format(self.date_time, self.tags, self.note, self.description)


# ***************** JSON ***********************
def convert_to_dict(obj):
    if isinstance(obj, ObjectId):
        return str(obj)

    note_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }

    note_dict.update(obj.__dict__)

    return note_dict


if __name__ == '__main__':
    app.run(debug=True)