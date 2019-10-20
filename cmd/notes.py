#!  /bin/python

import argparse
from datetime import datetime
import json
import requests

parser = argparse.ArgumentParser()
base_url = "http://localhost:5000"

def init_parser():
    parser.add_argument("note", help="The text you want to save", type=str)
    parser.add_argument("-t", "--tag", help="A tag for the note. Add multiple tags with multiple flags", type=str, action="append")
    parser.add_argument("-d", "--description", help="A description of the note", type=str)

def parse_cmd_args():
    args = parser.parse_args()
    #print(args)
    json_args = {
        'note': args.note,
        'date_time': str(datetime.today()),
        'tags': args.tag,
        'description': args.description
       }
    response = requests.post(base_url + "/notes", json=json_args )
    print(json_args)
    print(response.json())


init_parser()
parse_cmd_args()