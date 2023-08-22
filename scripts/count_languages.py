import matplotlib.pyplot as plt
from utils.getter import annotated_index, get_json_file, write_json, encode_json


def get_language(key):
    languages = get_json_file('languages.json')
    return languages[key]['language']


def init_count(j):
    for e in j:
        j[e]['count'] = 0
    return j


def increment_count(key, store):
    store[key]['count'] += 1
    return store


def display(data):
    languages = []
    counts = []
    for _, values in data.items():
        languages.append(values['language'])
        counts.append(values['count'])
    plt.bar(languages, counts)
    plt.show()



languages = get_json_file('languages.json')
languages = init_count(languages)

ai = annotated_index()


for entry in ai:
    details = ai[entry]['Entry Details']
    
    for key in languages:
        if key in details:
            languages = increment_count(key, languages)

write_json(languages, 'languages')
display(languages)
