import nltk 



from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree, word_tokenize,load_parser

'''
   1. Run pyStatParser first to get an approximation.
   2. From this approximation add to grammar.cfg
'''
#Grammar induction 
#sentence = "Smoking cocaine and pot is thrilling"
#sentence = 'Smoking cocaine and pot is thrilling'
sentence = "smoking_pot and cocaine is thrilling"
filename = 'test'
part1 = 'cocaine is pretty_sh$% in my_opinion'
part2 = 'you get some MMDA'
part3 = 'MDMA is a blank_canvas' 
part4 = 'you can do anything_you_want_with_it' 

parser = load_parser('grammar.fcfg')

for tree in parser.parse(part4.split()):
    tree.draw()
    print (tree)
