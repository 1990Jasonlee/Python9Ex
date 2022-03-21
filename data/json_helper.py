import os
import json
import pickle


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


def write_pickle(path):
    new_file = open('super_smash_characters.pickle', 'wb')
    pickle.dump(path, new_file)

write_pickle('/Users/jason/dev/Python9Ex/data')

def load_pickle(path):
    load_file = open(path, 'rb')
    data = pickle.load(load_file)
    return data

print(load_pickle('super_smash_characters.pickle'))