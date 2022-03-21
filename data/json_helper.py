import os
import json
def read_json(path):
    open_json = open(path)
    json_object = json.load(open_json)
    return json_object

def read_all_json_files():
