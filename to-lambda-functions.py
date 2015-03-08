import nltk, string 

from awesome_print import ap 
from stat_parser import Parser

from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree
from nltk import word_tokenize, load_parser

'''

	 1. Run pyStatParser first to get an approximation.
	 2. From thris approximation add to grammar.cfg

'''
#Grammar induction 
#sentence = "Smoking cocaine and pot is thrilling"
#sentence = 'Smoking cocaine and pot is thrilling'
#sentence = "1 agree with 2"
#sentence = "Moreover, dextromethorphan abuse is likely underreported to DAWN for 2 reasons."
sentence = 'dextromethorphan abuse' 
weasel_words = set(['moreover','likely'])
punkt = set(string.punctuation)
def deweasel(tokens):
	return [token for token in tokens if token.lower() not in weasel_words
		and not token.lower().isdigit()]

filename = 'for-lovasi'
approximation = False
if approximation:
	parser = Parser()
	tree = parser.parse(sentence)

	cf = CanvasFrame()
	tc = TreeWidget(cf.canvas(),tree)
	cf.add_widget(tc,20,20)
	cf.print_to_file('%s.ps'%filename)
	cf.destroy()

else:
	cp = load_parser('./bip-grammar.fcfg',trace=2)
	for tree in cp.parse(deweasel([token for token in word_tokenize(sentence) if token not in punkt])):
		tree.draw()
		'''
		semantic_value =  tree.label()['SEM']
		for item in semantic_value.predicates():
			print item.name
		for item in semantic_value.constants():
			print item.name
		'''
