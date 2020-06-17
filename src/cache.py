# Cache the results of searches to increase speed and decrease bandwidth load on thesaurus.com
# All requests for words go through cache.get
# 1. check the database for results
# 2. pass the query to requests.get
#
# Queries returned from requests.get will be cached with cache.put
import sqlite3, atexit, json, time, os.path
from eponym import interface

# SQLite3 DB setup
# _ prefix the database as it is not intended to be modified by a user
# unintentional effects caused by manual use could be bad for thesaurus.com
# __file__ is a realpath from /
db = sqlite3.connect(os.path.dirname(__file__) + "/.cache")
cursor = db.cursor()

# The database stores the search term, the timestamp, and returned synonyms in json format
cursor.execute("""
CREATE TABLE IF NOT EXISTS synonyms (
	base TEXT UNIQUE NOT NULL,
	ts INTEGER NOT NULL,
	syn TEXT
);
""")

@atexit.register
def _close():
	db.commit()
	db.close()

timeDelta = 15724800000# Data remains valid for 6 months (182 days)

# cache.put takes the base search term, it's synonyms, and combines them with a timestamp
# It then tries to insert or update data in the database
# Put returns no results
def put(base, syn):
	localTime = int(time.time())
	syn = json.dumps(syn)# Synonyms as an array is easiest to store in JSON
	try:
		cursor.execute("""
			INSERT INTO synonyms
			VALUES (?, ?, ?);
		""", (base, localTime, syn))
	except:
		cursor.execute("""
			UPDATE synonyms
			SET ts = ?,
					syn = ?
			WHERE base = ?;
		""", (localTime, syn, base))

# cache.get takes a single search term as input
# With standardized format from interface.normalize, it will search the database for a row with a valid time stamp
# If that fails, cache.get will pass the input term to interface.get and store the result in the database with cache.put.
# cache.get always returns the list of synonyms
def get(key, base):
	base = interface.normalize(base)
	try:# Get data from db
		ts, syn = cursor.execute("SELECT ts, syn FROM synonyms WHERE base = ?", (base, )).fetchall()[0]
		if time.time() - ts < timeDelta:
			return json.loads(syn)# Remember, it's stored as JSON
	except:# get data from API
		data = interface.get(key, base)
		syn = data["synonyms"]

		put(data["word"], data["synonyms"])# Store download in db

		return syn

# purge the cache of expired data points
def purge():
	meter = int(time.time()) - timeDelta
	cursor.execute("""
		DELETE FROM synonyms
		WHERE ts < ?;
	""", (meter, ))
