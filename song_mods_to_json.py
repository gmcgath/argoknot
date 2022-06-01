#Top-level module for converting song MODS XML to JSON


#Command line arguments:

#  --input file
#		The path to an XML file using the MODS schema
#  --output file
#		The path to a JSON file to be created

import sys
import argparse
from code.read_song_mods import *
from code.write_song_data import *

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='CSV file to parse', required=True)
parser.add_argument('--output', type=str, help='JSON file to create', required=True)
args = vars(parser.parse_args())

infile = args["input"]
outfile = args["output"]

#DEBUGGING CODE
print("Input: ", infile)
print("Output: ", outfile)

rsj = read_song_mods()
songs = rsj.read_mods_file(infile)
writer = WriteSongData()
with open(outfile, 'w') as f :
	for song in songs :
		writer.write_song(f, song)
	f.close()
