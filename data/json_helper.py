import os
import json
def read_json(path):
    open_json = open(path)
    json_object = json.load(open_json)
    return json_object

def read_all_json_files(path):
    json_list = []
    for files in os.walk(path):
        for file_in_question in files:
            if file_in_question.endswith('.json'):
                result = read_json(os.path.join(path, file_in_question))
                json_list.append(result)
    return json_list

