import nltk
from nltk import load_parser
cp = load_parser('NumbersTest.fcfg')
tokens = "Cocaine is good".split()
for tree in cp.parse(tokens):
    print (tree)
tokens2 = "Cocaines are good".split()
for tree in cp.parse(tokens2):
    print (tree)
tokens3 = "Cocaines is good".split()
for tree in cp.parse(tokens3):
    print (tree)
    if tree == "":
        print ("Error")
