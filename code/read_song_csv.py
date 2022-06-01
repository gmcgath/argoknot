#Read a song entry in CSV
#
#This reads one line of a CSV file and converts it to a Song
#
#Want input to be able to set its own mapping. 
#The constructor accepts a list of field names, which are associated
#with known field types.

#Looks like the csv library may be best suited to reading a whole file
#and returning a list (?) of lines.

#Is there any good way to put multiple values for a field into one line?
#Would need additional parsing. For now, assume no more than one.

import csv
from os.path import exists
from code.song import *

class ReadSongCsv :

	title_idx = -1;
	comp_idx = -1;
	lyr_idx = -1;
	album_idx = -1;
	tune_idx = -1;
	keyword_idx = -1;
	year_idx = -1;

	def __init__(self, mapping) :
		# All fields default to the empty string if not in the mapping
		title = ""
		comp = ""
		lyr = ""
		album = ""
		tune = ""
		keyword = ""
		year = ""
		mapping_len = len(mapping)
		for i in range(mapping_len) :
			item = mapping[i]
			if item == "title" :
				self.title_idx = i
			elif item == "composer" :
				self.comp_idx = i
			elif item == "lyricist" :
				self.lyr_idx = i 
			elif item == "album" :
				self.album_idx = i
			elif item == "tune" :
				self.tune_idx = i
			elif item == "keyword" :
				self.keyword_idx = i
			elif item == "year" :
				self.year_idx = i


# Read a CSV file at a specified path
	def read_csv_file(self, fil) :
		songs = []
		if not exists(fil) :
			print ("No such file: ", fil)
			return
		with open(fil, 'r') as csvfile :
			reader = csv.reader(csvfile)
			for row in reader :
				row_len = len(row)
				if self.title_idx >= 0 and self.title_idx < row_len :
					ttl = row[self.title_idx]
				else :
					ttl = ""
				if self.comp_idx >= 0 and self.comp_idx < row_len :
					comp = row[self.comp_idx]
				else :
					comp = ""
				if self.lyr_idx >= 0 and self.lyr_idx < row_len :
					lyr = row[self.lyr_idx]
				else :
					 lyr = ""
				if self.album_idx >= 0 and self.album_idx < row_len :
					alb = row[self.alb_idx]
				else  :
					alb = ""
				if self.tune_idx  >= 0 and self.tune_idx < row_len :
					tune = row[self.tune_idx]
				else  :
					tune = ""
				if self.keyword_idx >= 0 and self.keyword_idx < row_len :
					keyword = row[self.keyword_idx]
				else  :
					keyword = "" 
				if self.year_idx >= 0 and self.year_idx < row_len :
					year = row[self.year_idx] 
				else  :
					year = ""

				song = Song(ttl, comp, lyr, alb, tune, keyword, year)
				songs.append(song)
		return songs
