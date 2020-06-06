import bs4

# All entries in the database must be standardized
# no punctuation or capitalized characters are allowed
# extract.normalize picks out illegal characters from input text based on extract.legal
legal = range(97, 123)

def normalize(text):
	return ''.join([c for c in text.lower() if ord(c) in legal])

# Search through an html page from thesaurus.com to find synonym results
# convert the random tags into an array of useable data
def synonyms(plain):
	html = bs4.BeautifulSoup(plain, features="html.parser")
	if html.find(class_="no-results-title"): return None

	syn = html.find("h2").next_sibling
	if not syn: return None

	return [normalize(tag.string) for tag in syn.find_all(attrs={"data-linkid": "nn1ov4"}) if not ' ' in tag.string]