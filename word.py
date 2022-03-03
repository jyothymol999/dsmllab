import nltk
from nltk.tokenize import
sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import porterstemmer
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
text="""Hello Mr.Smith,how are you doing today? The weather is great,and city is awesome
The sky is pinkish_blue.you shouldn't eat cardboard"""
tokenized_word=word_tokenized(text)
print(tokenized_word)
stop_words=set(stopwords.words("english"))
print(stop_words)
filtered_word=[]
for w in tokenized_word:
if w not in stop_words:
filtered_word.append(w)
print("Tokenized Sentence:",tokenized_word)
print("filtered_Sentence:",filtered_word)
ps=porterstemmer()
