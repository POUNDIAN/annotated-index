import json

def get_json_file(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_backup_annotated_index():
    return annotated_index('backup/annotated-index.json')

def annotated_index(path='annotated-index.json'):
    return get_json_file(path)

def write_json(data, filename):
    if type(data) != bytes:
        data = encode_json(data)
    # takes data in form of bytes
    path = f'{filename}.json'
    with open(path, 'wb') as f:
        return f.write(data)

def encode_json(stuff):
    return json.dumps(stuff, indent=4).encode('utf-8')
