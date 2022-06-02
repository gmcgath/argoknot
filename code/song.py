# The Argoknot song class
# 
# A Song is a Python object which represents a song. 
# Most items are declared as list to allow multiple values.
# Nothing is required except the title. That is, all elements
# should be present, but they can have their default values,
# an empty list or a placeholder value.
#

import json
from json import JSONEncoder

class Song:
	title = ""
	composers = []
	lyricists = []
	performers = []
	album = []
	tune = []
	keywords = []
	comment = ""
	year = 0

	def __init__(self, ttl, cmp="", lyr="", per="", alb="", \
			tun="", kwd="", cmt="", yr=0) :
		self.title = ttl
		self.composers = cmp
		self.lyricists = lyr
		self.performers = per
		self.album = alb
		self.tune = tun
		self.keywords = kwd
		self.comment = cmt
		self.year = yr

#Some validation on a Song object. This will do things like exclude
#blank objects in a CSV import. For the moment at least, a Song is valid
#if it has a non-empty title.

	def is_valid (self) :
		return bool(self.title)


# The JSON encoder needs help serializing a custom object.
class SongJSONEncoder(JSONEncoder) :



	def default(self, song) :
		retval = {
			"title": song.title,
			"composers": song.composers,
			"lyricists": song.lyricists,
			"performers": song.performers,
			"album": song.album,
			"tune": song.tune,
			"keywords": song.keywords,
			"comment": song.comment,
			"year": song.year
		}
		return retval
