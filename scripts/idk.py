import re

from utils.getter import annotated_index

ai = annotated_index()

for entry in ai:
    page_numbers = ai[entry]["Page Numbers"]
    if re.match("[a-zA-Z]", page_numbers):
        print(f"{entry}: {page_numbers}")