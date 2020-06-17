import argparse, sys
import eponym

parser = argparse.ArgumentParser(description="Variable name generator")
parser.add_argument("words", nargs="+", help="list of input words")
parser.add_argument("-k", "--key", default=eponym.interface.APIKey.env, help="api key")
parser.add_argument("-l", "--lower", action="store_false", default=True, help="output lowercase")
parser.add_argument("-w", "--words", dest='w', action="count", default=1, help="output word count")
parser.add_argument("-s", "--sep", default='', help="word separator")
parser.add_argument("-m", "--max", default=sys.maxsize, type=int, help="maximum word length for each synonym")
args = parser.parse_args()

key = eponym.interface.APIKey(args.key)

syn = eponym.synonyms(key, ' '.join(args.words))
print(eponym.rand(syn, words=args.w, sep=args.sep, upper=args.lower, maxWordLength=args.max))
