import matplotlib.pyplot as plt

from utils.getter import annotated_index, get_json_file, write_json, encode_json

ai = annotated_index()
scores = {}

for entry in ai:
    references = ai[entry]['references']
    implicit_pages = ai[entry]['implicit_page_references']
    implicit_cantos = ai[entry]['implicit_canto_references']
    total = 0

    for ref in references:
        pages = ref['pages']
        total += len(pages)
    
    for ref in implicit_pages:
        pages = ref['pages']
        total += .5 * len(pages)
    
    for ref in implicit_cantos:
        pages = ref['pages']
        total += .1 * len(pages)
    
    scores[entry] = total

scores = sorted(scores.items(), key=lambda s: s[1], reverse=True)
scores = encode_json(scores)
write_json(scores, 'scores')


def display_scores():
    # kinda crummy
    scores = get_json_file('scores.json')
    values = []

    for elem in scores:
        score = elem[1]
        values.append(score)

    plt.hist(values)
    plt.show()

# display_scores()
