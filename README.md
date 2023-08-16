# annotated-index
Digitising The Annotated Index to The Cantos by Edwards and Vasse

## Creation

The raw text was generated by Amazon Textract (OCR); the photos were provided by physically photographing a copy of the Annotated Index. (?)

The raw was first formatted into JSON by ChatGPT. Note that ChatGPT introduced some details omitted by Edwards and Vasse. For example, the entry "Cuba" has canto & page numbers, but no detail. ChatGPT decided to provide some detail itself: "Island country in the Caribbean." (Also "Egypt", "England", ...)

## API and Database

The goal here is to provide a database and API which can provide all references in the Annotated Index concerning any given Canto. We also want to be able to look up reference and discover where it is referenced in The Cantos.

Though the An.Index is an outdated example of annotation for The Cantos, we intend to conglomerate all data for use instead of choosing only the most updated and accurate data. The cause for this can be read ...

## Manipulations

We will have to manipulate the data somewhat. Where the An.Index provides page number, we want to provide line number(s).

The An.Index uses capitalised words in the detail to suggest another entry. We want to be able to connect these entries somehow.

The An.Index uses square bracketted terms to denote that they actually don’t appear in a Canto, but might be a fundamental reference of another entry in a Canto. (Check the An.Index preface for this.)

There are also Canto Number / Page Numbers in square brackets. Investigate these.

Entries are not direct quotes from The Cantos. Edwards and Vasse reorders them into formats better suited for reference. Because entries can refer to multiple instances, they cannot always be direct quotes. At some point in the pipeline we need to provide the direct quote for highlighting. It might be good to have this in the per-Canto data.

We need to handle the entry "Emperor" which is not parseable. Currently: 

```json
"Emperor": {
    "Page Numbers": "18/80, 34/15, 38/41, 54/22, 54/25, 54/28, 54/32, 55/39, 55/41, 55/43, 55/44, 56/52, 56/56, 57/60, 58/63, 58/65, 60/74, 60/78, 61/80, 61/81, 61/82, 61/85",
    "Entry Details": "Various emperors mentioned throughout the text."
  },
```

From the An.Index:

```txt
 Emperor 9/34: see SIGISMUND V, Holy Roman Emperor. 
 Emperor: 
 18/80: see KUBLAI KHAN. 
 Emperor: 34/15: see ALEXANDER I, of Russia. 
 Emperor: 38/41: see NAPOLEON III. 
 Emperor: 54/22: see KAO-HOANG-TI. 
 Emperor: 54/25: see HAN-SIUEN-TI. 
 Emperor: 54/28: see TCIN OU TI 
 Emperor: 54/32: see TAI-TSONG. 
 EMPEROR 
 [60] 
 Emperor: 55/39: see CHEKING-TANG. 
 Emperor. 55/41: see TAI-TSQU. 
 Emperor 55/43, 44. see CHIN-TSONG. 
 Emperor 56/52: see GIN-TSONG. 
 Emperor: 56/56 see INGAIYCOU-CHILITALA. 
 Emperor 57/60: see OU-TSONG. 
 Emperor: 58/63 see CHIN-TSONG. 
 Emperor 58/65. see TAI-TSONG. 
 Emperor 60/74, 78 see KANG-HI. 
 Emperor 61/80,81,82 see YONG-TCHING. 
 Emperor. 61/85: see KIEN-LONG. 
 Emperor 65/125, 69/150, 151 see FREDERICK II, of Prussia. 
```

Edit: I think at other points ChatGPT has allowed us multiple same keys; that makes the JSON invalid but at least we have all the information.

We also have instances of, e.g., "See Appendix A."

ChatGPT also gave the following warning:

```txt
Please note that there are duplicate keys "Pierre" and "Pio" in your provided data. JSON objects cannot have duplicate keys, so I've retained the last instance of each duplicate key in the JSON representation. If you need to handle these duplicates differently, you might need to adjust your data structure or key names accordingly.
```

We need to investigate what data might have been dropped.

## Errors

There are some flaws in the Textract output and the data will need cleaning at some point. One common example is the substitution of '1' for 'i' or 'I'. A common example is "1S", but I'm sure there are more. We also have instances of invalid brackets (in page numbers), for example `"a/b]"`

We might want to provide a way for users to suggest there is an error in an entry. Given a hit, we can manually check with a copy of the book.

ChatGPT uses the token '(?)' where it cannot discern a word. We need to go through and fix these. Wait: seems they are in the raw. Maybe they were in the An.Index.

ChatGPT uses the token 'Unknown' for Page Number where it has failed to parse. We need to go through and fix these too.

Might also see entries such as this (if I made a mistake):

```json
  "DOUGLAS": {
    "Page Numbers": "[54]",
    "Entry Details": "Incomplete reference, likely referring to someone named Douglas."
  },
```

Question: Do page numbers with hyphens survive the parse?

Sometimes `"N/A"` is used for an empty entry, sometimes `null`.

Also seems there are some special characters, for example `\n` that slip in. Need to understand our handling of these; probably an OCR mistake requiring correction.

## Suggested Measurements

[poundian#142](https://github.com/louisdeb/poundian/issues/142) suggests counting the number of translations by language.

We can also count the number of references by Page Number length & see if we have any insight into the most used material. This count can be extended by observing references in Entry Details of other entries. We might want to count how many entries are referenced by other entries, i.e. secondary references that accumulate attention on the primary entry. Then there are also non-obvious references, such as 'See Inferno' which makes no mention of 'Dante' (entry: "si com' ad Arli: 80/86: (It) so as at ARLES. (See: Inferno, 9, 112).")

So we might want to store this JSON parse in a dynamo db. That will allow us to query it from multiple different programs and have one updatable data. TAI is so behind TCP that I don't know if it can form a basis for better annotation, although TAI might have more entries than TCP?

Obviously if we have a db we especially need to handle having duplicate keys.

Also if we have a db we can have an API that can return us e.g. per-Canto annotations.

## Otherwise

So much of the work done so far and so many of the suggestions here would become lightweight if we had money to use GPT in pipeline.
