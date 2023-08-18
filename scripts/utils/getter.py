import json

def annotated_index():
    path = "../annotated-index.json"
    with open(path, "r") as f:
        return json.load(f)
