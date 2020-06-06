# Cache the results of searches to increase speed and decrease bandwidth load on thesaurus.com
# All requests for words go through cache.get
# 1. check the database for results
# 2. pass the query to requests.get
#
# Queries returned from requests.get will be cached with cache.put
# after being filtered by extract.synonyms
import sqlite3, atexit, json, time, os.path, requests as req
from eponym import extract

# SQLite3 DB setup
# _ prefix the database as it is not intended to be modified by a user
# unintentional effects caused by manual use could be bad for thesaurus.com
_db = sqlite3.connect(os.path.dirname(__file__) + "/.cache")
_crsr = _db.cursor()

# The database stores the search term, the timestamp, and returned synonyms in json format
_crsr.execute("""
CREATE TABLE IF NOT EXISTS synonyms (
	base TEXT UNIQUE,
	ts INTEGER,
	syn TEXT
);
""")

@atexit.register
def _close():
	_db.commit()
	_db.close()

url = "https://thesaurus.com/browse/{}"
timeDelta = 15724800000# Data remains valid for 6 months (182 days)

# cache.put takes the base search term, it's synonyms, and combines them with a timestamp
# It then tries to insert or update data in the database
# Put returns no results
def put(base, syn):
	base = extract.normalize(base)# Data must be standardized in the database
	localTime = int(time.time())
	syn = json.dumps(syn)# Synonyms as an array is easiest to store in JSON
	try:
		_crsr.execute("""
			INSERT INTO synonyms
			VALUES (?, ?, ?);
		""", (base, localTime, syn))
	except:
		_crsr.execute("""
			UPDATE synonyms
			SET ts = ?,
					syn = ?
			WHERE base = ?;
		""", (localTime, syn, base))

# cache.get takes a single search term as input
# With standardized format from extract.normalize, it will search the database for a row with a valid time stamp
# If that fails, cache.get will pass the input term to requests.get, extract the synonyms from the html code and store the result in the database with cache.put.
# cache.get always returns the list of synonyms
def get(base):
	base = extract.normalize(base)
	# Get data from db
	try:
		ts = _crsr.execute("SELECT ts FROM synonyms WHERE base = ?", (base, )).fetchall()[0][0]
		if time.time() - ts < timeDelta:
			syn = _crsr.execute("SELECT syn FROM synonyms WHERE base = ?", (base, )).fetchall()[0][0]
			return json.loads(syn)# Remember, it's stored as JSON
	finally:
		data = req.get(url.format(base))
		syn = extract.synonyms(data.text)

		put(base, syn)# Store download in db

		return syn