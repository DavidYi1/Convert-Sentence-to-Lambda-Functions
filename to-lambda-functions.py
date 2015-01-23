import nltk 

from awesome_print import ap 
from stat_parser import Parser

from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree
from nltk import word_tokenize

'''

   1. Run pyStatParser first to get an approximation.
   2. From thris approximation add to grammar.cfg

'''
#Grammar induction 
#sentence = "Smoking cocaine and pot is thrilling"
#sentence = 'Smoking cocaine and pot is thrilling'
sentence = "John saw Mary"
filename = 'test'

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
  #sentence = nltk.word_tokenize(sentence)
  sentence = ['smoking','pot','and','cocaine','is','thrilling']
  grammar = nltk.data.load('./grammar2.cfg')

  parser = nltk.ChartParser(grammar)
  dotname = '%s.dot'%(filename)
  for tree in parser.parse(sentence):
    tree.draw()
  '''
  with open(dotname,'wb') as outfile:
    print>>outfile,parses.dot_digraph()
  '''