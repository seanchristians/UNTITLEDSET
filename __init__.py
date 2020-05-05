from eponym import cache, extract

class Synonyms:
	def __init__(self, sentence):
		self.sentence = sentence
		self.syn = []
		for base in sentence.split(' '):
			self.syn += cache.get(base)