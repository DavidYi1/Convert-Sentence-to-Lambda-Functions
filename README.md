# Convert-Sentence-to-Lambda-Functions
import nltk
grammar = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP 
  V -> "is" 
  Adj -> "Smoking"
  Coj -> "and"
  Nom -> Adj Nom | N
  NP ->  Nom Coj NP | N
  Det -> "a" | "an" | "the" | "my"
  N -> "cocaine" | "pot" | "thrilling"
  P -> "in" | "on" | "by" | "with"
  """)
sent = "Smoking cocaine and pot is thrilling".split()
rd_parser = nltk.RecursiveDescentParser(grammar, )
for tree in rd_parser.parse(sent):
    print (tree)
    
    
