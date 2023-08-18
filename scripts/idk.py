import re
import collections

from utils.getter import annotated_index

ai = annotated_index()
missed = {}

for entry in ai:
    page_numbers = ai[entry]["Page Numbers"]
    search = re.findall("\d+\/", page_numbers)
    if search:
        # Remove '/'
        search = [s[:-1] for s in search]

        # Save to entry
        ai[entry]["cantos"] = search

        # This loses information if we have multiple instances in one canto.
    else:
        missed[entry] = ai[entry]

# print(ai)
print(missed)
