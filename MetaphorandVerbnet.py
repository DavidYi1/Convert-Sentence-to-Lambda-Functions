import nltk 
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree, word_tokenize,load_parser
from nltk.corpus import verbnet as vn
verbsenses = (vn.classids('run'))

metaphor1 = " I run a race" 
metaphor2 = " I run an errand" 
parser = load_parser('grammar.fcfg')
for tree in parser.parse(metaphor1.split()):
    lambdaexpression = (tree.label()['SEM'])
for word in metaphor1.split():
    if vn.classids(word) != []:
        start = set(vn.classids(word))
        for i in start:
            if i == verbsenses:
                del i
            final = list(start)
print (lambdaexpression,final)
    
for tree in parser.parse(metaphor2.split()):
    lambdaexpression = (tree.label()['SEM'])
for word in metaphor2.split():
    if vn.classids(word) != []:
        start = set(vn.classids(word))
        for i in start:
            if i == verbsenses:
                del i
            final = list(start)
print (lambdaexpression,final)

if final == verbsenses:
    sense = "metaphor"
    print (sense) ##It should print out metaphor but doesn't.
