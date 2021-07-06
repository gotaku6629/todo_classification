import numpy as np
import gensim

import os
# os.system('ls')
# os.system('ls ../')

MODEL = gensim.models.KeyedVectors.load_word2vec_format('entity_vector/entity_vector.model.bin', binary=True)
CATEGORY_LIST = ('勉強', '授業', '研究', '遊び', '旅行', '就活')
def classify(text):
    print(text)
    # try:
    similarities = [MODEL.similarity(text, c) for c in CATEGORY_LIST]
    print(similarities)
    category = CATEGORY_LIST[np.argmax(similarities)]
    
    return category
    # except KeyError:
    #     return 'その他'


    if len(text) > 3:
        return '勉強'
    else:
        return '遊び'