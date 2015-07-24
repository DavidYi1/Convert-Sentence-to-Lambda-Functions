import nltk 

from awesome_print import ap 
from stat_parser import Parser

from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree, word_tokenize,load_parser

'''

   1. Run pyStatParser first to get an approximation.
   2. From thris approximation add to grammar.cfg

'''
#Grammar induction 
#sentence = "Smoking cocaine and pot is thrilling"
#sentence = 'Smoking cocaine and pot is thrilling'
sentence = "smoking_pot and cocaine is thrilling"
sentence = "I smoke pot"
filename = 'test'

parser = load_parser('./grammar.fcfg', trace=2)

for tree in parser.parse(sentence.lower().split()):
	ap('bob')
	tree.draw()