import nltk 

from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree, word_tokenize,load_parser

part1 = 'cocaine is pretty_sh$% in my_opinion'
part2 = 'get some_MMDA'
parser = load_parser('grammar.fcfg')

for tree in parser.parse(part1.split()):
    tree.draw()
    print (tree)

