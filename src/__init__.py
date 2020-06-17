from eponym import cache
import random, sys

def synonyms(key, sentence=''):
	sentence = sentence.split(' ') if len(sentence) > 0 else ''
	syn = []
	for base in sentence:
		syn += cache.get(key, base)
	return syn

def rand(syn, *, words=1, sep='', upper=False, maxWordLength=sys.maxsize):
	var = ['']
	for i in range(words):
		c = ''
		while c in var or len(c) > maxWordLength:
			c = random.choice(syn)

		var.append(c.upper() if upper else c)
	return sep.join(var)[len(sep):]
