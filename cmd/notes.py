#!  /bin/python

import argparse
import json
import requests

parser = argparse.ArgumentParser()
base_url = "http://localhost:5000"

def init_parser():
    # TODO add operation (add, get all, get single, get by tag(s))
    parser.add_argument("note", help="The text you want to save", type=str)
    # TODO change default tag behaviour
    parser.add_argument("-t", "--tag", help="A tag for the note. Add multiple tags with multiple flags", type=str, action="append",default=["general"])
    parser.add_argument("-d", "--description", help="A description of the note", type=str)

def parse_cmd_args():
    args = parser.parse_args()
    json_args = {
        'note': args.note,
        'tags': args.tag,
        'description': args.description
       }
    response = requests.post(base_url + "/notes", json=json_args )
    print(response.json())


init_parser()
parse_cmd_args()