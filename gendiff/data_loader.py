import json
import yaml


def recognize(data, extension):
    if extension == 'json':
        return json.load(data)
    elif extension == 'yaml' or extension == 'yml':
        return yaml.load(data, Loader=yaml.FullLoader)
    else:
        raise Exception('Unknown file extension. Please try again. '
                        'Available extensions: json, yaml.')
