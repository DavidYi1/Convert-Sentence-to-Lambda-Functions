import nltk 
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree, word_tokenize,load_parser
from nltk.corpus import verbnet as vn

metaphor1 = " I run a race" 
metaphor2 = " I run an errand" 
parser = load_parser('NewGrammar.fcfg')
for tree in parser.parse(metaphor1.split()):
    lambdaexpression = (tree.label()['SEM'])
print(lambdaexpression)

parsed = lambdaexpression
for p in parsed.predicates():
    print(p)
    
text = word_tokenize(metaphor1)
tag = nltk.pos_tag(text)
print(tag)
for word in tag:
    if word[1] == 'VBP':
        print (word[0])
