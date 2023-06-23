import json

def json_formatter(diff):

    js = json.JSONEncoder.encode(diff)
    print(js)