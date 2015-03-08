
metaphor1 = " I run a race" 
metaphor2 = " I run an errand" 
parser = load_parser('grammar.fcfg')

for tree in parser.parse(metaphor1.split()):
    print (tree.label()['SEM'])
for tree in parser.parse(metaphor2.split()):
    print (tree.label()['SEM'])

from nltk.corpus import verbnet as vn
print (vn.classids('run'))
v = vn.vnclass('run-51.3.2')
print (vn.lemmas('run-51.3.2'))
print (vn.pprint_themroles('run-51.3.2')) #Obtain the theme of verb "run"
print([t.attrib['type'] for t in v.findall('THEMROLES/THEMROLE')])

for word in metaphor1.split():
    if vn.classids(word) != []:##Very interesting part here.
        
        
        print (vn.classids(word))# It returns the same as print (vn.classids('run')) 
                                 #but also returns the actual sense used in context.
for word in metaphor2.split():
    if vn.classids(word) != []:
        print (vn.classids(word))
