import json

file = open('annotated-index.json', 'r')
ai = json.load(file)

for key in ai.keys():
    entry = ai[key]
    annotation = str(entry['Entry Details'])
    if len(annotation) > 2:
        annotation = annotation[0].upper() + annotation[1:]
    entry['Entry Details'] = annotation
    ai[key] = entry

with open('annotated-index.json', 'w+') as out:
    json.dump(ai, out, indent=4, ensure_ascii=False)
    