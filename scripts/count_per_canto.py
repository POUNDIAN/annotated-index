import json

def count_per_canto():
    file = open('annotated-index.json', 'r')
    ai = json.load(file)
    accrue = {}
    for k in ai.keys():
        entry = ai[k]
        for ref in entry['references']:
            canto = int(ref['canto'])
            if canto in accrue.keys():
                accrue[canto] += 1
            else: accrue[canto] = 1
    
    accrue = dict(sorted(accrue.items()))
    print(accrue)

count_per_canto()
