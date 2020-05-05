import bs4

def normalize(text):
	legal = range(97, 123)
	return ''.join([c for c in text.lower() if ord(c) in legal])

def synonyms(plain):
	html = bs4.BeautifulSoup(plain, features="html.parser")
	if html.find(class_="no-results-title"): return None

	syn = html.find("h2").next_sibling
	if not syn: return None

	return [normalize(tag.string) for tag in syn.find_all(attrs={"data-linkid": "nn1ov4"}) if not ' ' in tag.string]