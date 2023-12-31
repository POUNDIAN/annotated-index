import json
import re

from utils.getter import annotated_index, write_json


def parse_canto_and_pages(text):
    # This pattern drops any instances of '(?)' following page numbers,
    # i.e. if E&V are unsure of the reference. We assume the reference.
    pattern = r'(\[?\d+\]?)\/(\[?\d+\]?)|(\[?\d+\]?)'

    matches = re.findall(pattern, text)
    results = {}
    current_canto = None
    
    for match in matches:
        if match[0]:  # Matched canto/page_number combination
            canto = match[0]
            page_number = match[1]
        elif match[2]:  # Matched single page number
            canto = current_canto
            page_number = match[2]
        else:
            continue
        
        if canto not in results:
            results[canto] = []
        
        results[canto].append(page_number)
        current_canto = canto
    
    return results


def get_references(items):
    references = []
    implicit_page_references = []
    implicit_canto_references = []

    # Used to handle multiple implicit Cantos, e.g. [56/49, 77/45]
    extended_implicit = False

    for canto, pages in items:
        if '[' in canto or extended_implicit:
            # Build implicit references
            extended_implicit = ']' not in pages[-1] and '[' not in pages[-1]
            canto = canto.replace('[', '')
            pages = [page.replace(']', '') for page in pages]
            implicit_canto_references.append({'canto': canto, 'pages': pages})

        else:
            # Separate implicit and non-implicit page references
            implicit_pages = []
            non_implicit_pages = []
            
            for page in pages:
                if '[' in page:
                    implicit_pages.append(page.replace('[', '').replace(']', ''))
                else:
                    non_implicit_pages.append(page)

            if implicit_pages:
                implicit_page_references.append({'canto': canto, 'pages': implicit_pages})
            references.append({'canto': canto, 'pages': non_implicit_pages})
    
    return references, implicit_page_references, implicit_canto_references


ai = annotated_index()
new = {}

for entry in ai:
    page_numbers = ai[entry]['Page Numbers']

    try:
        details = ai[entry]['Entry Details']
    except KeyError:
        details = ''

    cleaned_page_numbers = page_numbers.replace(' ', '')
    cleaned_page_numbers = cleaned_page_numbers.replace(';', ',')

    results = parse_canto_and_pages(cleaned_page_numbers)    

    references, implicit_page_references, implicit_canto_references = get_references(results.items())

    values = {
        'Page Numbers': page_numbers,
        'Entry Details': details,
        'references': references,
        'implicit_page_references': implicit_page_references,
        'implicit_canto_references': implicit_canto_references,
    }

    new[entry] = values

new = json.dumps(new, ensure_ascii=False, indent=4).encode('utf-8')
write_json(new, 'annotated-index')
