import json

def get_backup_annotated_index():
    return annotated_index('../backup/annotated-index.json')

def annotated_index(path='../annotated-index.json'):
    with open(path, 'r') as f:
        return json.load(f)

def write_json(data, filename):
    # takes data in form of bytes
    path = f'../{filename}.json'
    with open(path, 'wb') as f:
        return f.write(data)
