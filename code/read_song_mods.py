# Read a song file in XML, using the Library of Congress MODS schema

from os.path import exists
from xml.dom import minidom
from code.song import *

class read_song_mods :


	domdoc = False;
	items = False;
	domidx = 0;

# Fields of a song. Performer will always be blank for a songbook,
# but needs to be here to make the function call.
	song = False
	ttl = False
	comp = ""
	lyr = "" 
	per = ""
	alb = ""
	tune = ""
	keyword = ""
	year = ""

# Constructor. 
	def __init__(self) :
		return

# Read a file with a specified path and return a list of JSON song items
	def read_mods_file (self, fil) :
		songs = []
		if not exists(fil) :
			print ("No such file: ", fil)
			return songs
		try:
			domdoc = minidom.parse(fil);
		except:
			print ("Error openng file ", fil)
			return songs
		items = domdoc.getElementsByTagName("relatedItem")
		for item in items :
			if item.getAttribute("type") == "constituent" :
				songs.append(self.item_to_json(item))
		return songs

# Takes a MODS relatedItem and converts it to a song in JSON
	def item_to_json(self, item) :
		subelems = item.childNodes
		for subelem in subelems :
			elem_name = subelem.nodeName
			if elem_name == "titleInfo" :
				self.get_title(subelem)
			elif elem_name == "name" and subelem.getAttribute("type") == "personal" :
				self.get_names(subelem)
			elif elem_name == "relatedItem" and subelem.getAttribute("type") == "preceding" :
				self.get_tune(subelem)

			# much more to do. Probably want to decompose
		if self.ttl :
			song = Song(self.ttl, \
				self.comp, \
				self.lyr, \
				self.alb, \
				self.per, \
				self.tune, \
				self.keyword, 
				self.year)
		return song

#Extract the title from the titleInfo element. Set self.ttl if a title found.
	def get_title(self, title_info) :
		title_elems = title_info.childNodes
		for sub_elem2 in title_elems :
			if sub_elem2.nodeName == "title" :
				text_node = sub_elem2.firstChild
				if text_node :
					self.ttl = text_node.nodeValue.strip()

#Extract names from tne name element. Can set comp and lyr.
#This version gets just one composer and one lyricist. Next version should support
#multiple composers and lyricists.
	def get_names(self, name_elem) :
		comp_type = False
		lyr_type = False
		pers_name = ""
		name_elems = name_elem.childNodes
		for sub_elem2 in name_elems :
			if sub_elem2.nodeName == "namePart" :
				text_node = sub_elem2.firstChild
				if text_node :
					pers_name = pers_name + text_node.nodeValue.strip()
			elif sub_elem2.nodeName == "role" :
				role_elems = sub_elem2.childNodes
				for role_elem in role_elems :
					if role_elem.nodeName == "roleTerm" :
						role_text_node = role_elem.firstChild
						if role_text_node :
							role_term = role_text_node.nodeValue.strip()
						if role_term == "composer" :
							comp_type = True
						elif role_term == "lyricist" :
							lyr_type = True
		if comp_type :
			self.comp = pers_name
		elif lyr_type :
			self.lyr = pers_name

#Extract the tune's title from the relatedItem "preceding" element.
#This looks just like the song's top-level element, but all we're interested
#in right now is the title. (Should this change? Should we pull out the
#tune's composer and put it in as the song's composer? Probably.
#This should be generalized to support multiple tunes.
	def get_tune(self, related_elem) :
		sub_elems = related_elem.childNodes
		for subelem in sub_elems :
			elem_name = subelem.nodeName
			if elem_name == "titleInfo" :
				self.get_tune_title(subelem)

#Extract the title from the titleInfo element. This one is for the tune.
	def get_tune_title(self, title_info) :
		title_elems = title_info.childNodes
		for sub_elem2 in title_elems :
			if sub_elem2.nodeName == "title" :
				text_node = sub_elem2.firstChild
				if text_node :
					self.tune = text_node.nodeValue.strip()
