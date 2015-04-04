import nltk 
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree, word_tokenize,load_parser
from nltk.corpus import verbnet as vn
from nltk.corpus import wordnet as wn
from nltk.corpus import verbnet 
from nltk.wsd import lesk
from nltk.corpus import framenet as fn
from pprint import pprint


metaphor1 = " I run a race" 
metaphor2 = " I run an errand" 
parser = load_parser('NewGrammar.fcfg')
for tree in parser.parse(metaphor1.split()):
    lambdaexpression = (tree.label()['SEM'])
print(lambdaexpression)


parsed = lambdaexpression
predicates_from_parsed =[]
swag =[]
verbs=[]

for p in parsed.predicates():
    print(p)
    swag.append(p)
for word,pos in nltk.pos_tag(nltk.word_tokenize(metaphor1)):
    initial = metaphor1.split
    if 'V' in pos: #Another way to focus on only verbs
            verbs.append(word)
print(verbs)
print(nltk.pos_tag(nltk.word_tokenize(metaphor1)))
for word,pos in nltk.pos_tag(nltk.word_tokenize(metaphor1)):
    print (word,'\t')
    if "N" in pos:
        pos = "n"
    if "V" in pos:
        pos = "v"
    print (lesk(metaphor1, word, pos))## Trying to use for sense identification

for word in verbs:
    final = [sense for sense in vn.classids(word)]
    print (final)
    for sense in final:
        x = vn.lemmas(sense)
        print (x)
        #for thing in x:
        #   print (fn.lus(r'(?i)%s'%(x)))

run_senses = {'meander-47.7': 'figurative', 
'preparing-26.3-1':'figurative',
'run-51.3.2': 'literal',
'swarm-47.5.1-1': 'figurative'
}

for x in final:
    print(run_senses[x])


for x in nltk.word_tokenize(metaphor1):
    print (fn.lus(r'(?i)%s'%(x)))
print (fn.lus('race'))

