#Top-level module for converting song CSV to JSON

#The CSV fields are specified in the command line with "-fields" followed by
#field names. Any command line argument starting with "-" terminates the field list.

#Command line arguments:

#  --input file
#		The path to a CSV file
#  --output file
#		The path to a JSON file to be created
#  --fields f1 f2 ...
#	The sequence of field names. Acceptable names are:
#		title 
#		composer 
#		lyricist 
#		performer 
#		album 
#		tune 
#		keywords 
#		year
#
# In its present form, it allows just one value per field. Need to
# explore ways to improve this.

import sys
import argparse
from code.read_song_csv import *
from code.write_song_data import *

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='CSV file to parse', required=True)
parser.add_argument('--output', type=str, help='JSON file to create', required=True)
parser.add_argument('--fields', nargs='*', help='Sequence of fields in each row', \
	required=True)
args = vars(parser.parse_args())

infile = args["input"]
outfile = args["output"]
fields = args["fields"]

#DEBUGGING CODE
print("Input: ", infile)
print("Output: ", outfile)
print("Fields: ", fields)

rcsv = ReadSongCsv(fields)
songs = rcsv.read_csv_file(infile)
writer = WriteSongData()
with open(outfile, 'w') as f :
	for song in songs :
		writer.write_song(f, song)
	f.close()
