import numpy as np
import gensim
from janome.tokenizer import Tokenizer
# from nltk.corpus import stopwords
import os
# os.system('ls')
# os.system('ls ../')

MODEL = gensim.models.KeyedVectors.load_word2vec_format('https://github.com/gotaku6629/todo_classification/releases/download/v0.1/entity_vector.model.bin', binary=True)
CATEGORY_LIST = ('勉強', '授業', '研究', '遊び', '旅行', '就活')
TOKENIZER = Tokenizer()
# STOPWORDS = stopwords.words('japanese')

def classify(text):
    print('text: ', text)
    token = TOKENIZER.tokenize(text)
    texts = [w.surface for w in token if w.part_of_speech[0] in ('名', '動', '形')]
    # texts = [w.surface for w in token if w not in STOPWORDS]

    print('texts: ', texts)
    # try:
    similarities = np.array([[MODEL.similarity(text, c) for c in CATEGORY_LIST] for text in texts])
    print('similarites: ', similarities)
    category = CATEGORY_LIST[np.argmax(np.max(similarities, axis=0))]
    
    return category
    # except KeyError:
    #     return 'その他'


    # if len(text) > 3:
    #     return '勉強'
    # else:
    #     return '遊び'