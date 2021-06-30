import numpy as np
import gensim

def classify(text):
    if len(text) > 3:
        return '勉強'
    else:
        return '遊び'