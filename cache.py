import sqlite3, atexit, json, time, os.path, requests as req
from eponym import extract

# SQLite3 DB setup
_db = sqlite3.connect(os.path.dirname(__file__) + "/.cache")
_crsr = _db.cursor()

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
timeDelta = 604800000# Data remains valid for 1 week

def put(base, syn):
	base = extract.normalize(base)
	localTime = int(time.time())
	syn = json.dumps(syn)
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

def get(base):
	base = extract.normalize(base)
	# Get data from db
	try:
		ts = _crsr.execute("SELECT ts FROM synonyms WHERE base = ?", (base, )).fetchall()[0][0]
		if time.time() - ts < timeDelta:
			syn = _crsr.execute("SELECT syn FROM synonyms WHERE base = ?", (base, )).fetchall()[0][0]
			return json.loads(syn)
	finally:
		data = req.get(url.format(base))
		syn = extract.synonyms(data.text)

		put(base, syn)# Store download in db

		return syn