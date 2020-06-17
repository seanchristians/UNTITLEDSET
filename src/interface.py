# Keep all api-interfacing code in one file
import requests, os

class APIKey:
	env = "APIKEY"

	def __init__(self, key=env):
		key = key[1:] if key[0] == '$' else key# The '$' character is only useful in shell scripts

		if key in os.environ:# environment variable
			self.key = os.environ[key]

		elif os.path.isfile(key):# key stored in local file
			with open(key, 'r') as f:
				self.key = f.read()

		elif len(key) > 0 and type(key) is str:# key provided as direct input
			self.key = key

		else:
			raise Exception("API key not declared in this scope")# missing key is fatal

# All entries in the database must be standardized
# no punctuation or capitalized characters are allowed
# extract.normalize picks out illegal characters from input text based on interface.legal
legal = range(97, 123)

def normalize(text):
	return ''.join([c for c in text.strip().lower() if ord(c) in legal])

def get(key, word):
	url = "https://wordsapiv1.p.rapidapi.com/words/{}/synonyms"
	headers = {
		"x-rapidapi-host": "wordsapiv1.p.rapidapi.com",
		"x-rapidapi-key": key.key
	}

	response = requests.request(
		"GET",
		url.format(word),
		headers=headers
	)

	return response.json()
