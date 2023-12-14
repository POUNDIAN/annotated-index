import json
    

def convert_refs_to_int():
    file = open('annotated-index copy.json', 'r')
    ai = json.load(file)

    def convert(refs):
        converted = []
        for ref in refs:
            ref['canto'] = int(ref['canto'])
        
            pages = []
            for page in ref['pages']:
                page = page.replace('[', '').replace(']', '')  # debris
                pages.append(int(page))
            ref['pages'] = pages

            converted.append(ref)
        return converted

    new = {}
    for k in ai.keys():
        entry = ai[k]
        entry['references'] = convert(entry['references'])
        entry['implicit_page_references'] = convert(entry['implicit_page_references'])
        entry['implicit_canto_references'] = convert(entry['implicit_canto_references'])
        new[k] = entry
    
    with open('annotated-index.json', 'w+') as o:
        json.dump(new, o, indent=4, ensure_ascii=False)


convert_refs_to_int()