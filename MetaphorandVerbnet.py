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
for word,pos in nltk.pos_tag(nltk.word_tokenize(metaphor1)):
    if 'V' in pos: #Another way to focus on only verbs
       final = [sense for sense in vn.classids(word) if 'run' in sense]
       print (final)
       final = str(final).strip('['']')
       print (final)
       unnatural = (vn.pprint_themroles('run-51.3.2'))
       #print ((vn.pprint_themroles(final)))
       
print (lambdaexpression,final)
    
for tree in parser.parse(metaphor2.split()):
    lambdaexpression = (tree.label()['SEM'])
for word,pos in nltk.pos_tag(nltk.word_tokenize(metaphor2)):
    if 'V' in pos: #Another way to focus on only verbs
       final = [sense for sense in vn.classids(word) if 'run' in sense]
       print (final)
       final = str(final).strip('['']')
       print (final)
       unnatural = (vn.pprint_themroles('run-51.3.2'))
       #print ((vn.pprint_themroles(final)))
print (lambdaexpression,final)
