# Write song entry in JSON
# Can I do this without assigning internal IDs? It would make things easier
# and less fragile.

# If all data on a song is here, can do it. The only problem is enforcing
# restricted vocabularies. Or maybe I don't.


# This operates on an object of the Song class. Or really any object.
# It doesn't really need to be a class, but it is just for consistency.
import json
from code.song import *

class WriteSongData :

	def __init__(self) :
		return

	def write_song(self, fil, song) :
		json_text = json.dumps(song, indent=4, cls=SongJSONEncoder)
		fil.write(json_text)
		fil.write("\n")
