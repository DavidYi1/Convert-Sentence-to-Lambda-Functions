from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer 
fid = open("marjiuana based tweets.txt","r")

seperate_tweets = fid.readlines() #If want each tweet seperate
fid.close()


combined_tweets = []
fid = open("marjiuana based tweets.txt","r")
combined_tweets.append(str(fid.readlines())) ##In case looking at tweets in general 
fid.close()

char = "//t.co/"

tokenized_docs = [word_tokenize(doc) for doc in seperate_tweets]
for item in tokenized_docs:
    [word.replace('\\n', '') for word in item]##Works only for seperate tweets
     ##All of the line breaks that are included with the word is now removed
    for word in item:
        if char in word:
            item.remove(word)
print (tokenized_docs)

    
        
punctuation = [".",",","'",'"','``','#',"-","(",")","http",':'] ## Will also remove the hashtag symbol. 
##Punctuation also removes part of the http part of the link

tokenized_docs_no_stopwords = []
for doc in tokenized_docs:
    new_term_vector = []
    for word in doc:
        if not word in stopwords.words('english'):
            if not word in punctuation:
                new_term_vector.append(word)
    tokenized_docs_no_stopwords.append(new_term_vector)
            
print (tokenized_docs_no_stopwords)

wordnet = WordNetLemmatizer()

preprocessed_docs = []

for doc in tokenized_docs_no_stopwords:
    final_doc = []
    for word in doc:
        final_doc.append(wordnet.lemmatize(word)) #note that lemmatize() can also takes part of speech as an argument!
    preprocessed_docs.append(final_doc)

print (preprocessed_docs)
