"""
initialized pre trained models here
"""
import os
import pickle
import lzma
from traceback import format_exc

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))



def load_pickle(f):
    try:
        path = os.path.join(__location__, f)
        with open(path, 'rb') as p:
            unpickled = pickle.load(p)
        return unpickled
    except Exception as ex:
        tb = format_exc()
        print(tb)

# def nearestneighbors():
#     f = 'nearestneighbors.pkl.xz'
#     p = load_pickle(f)
#     return p

def multiNB():
    f = 'multinomialNB.pkl'
    p = load_pickle(f)
    return p

def vectorizer():
    f = 'TfidfVectorizer.pkl'
    p = load_pickle(f)
    return p

def vocab():
    f = 'vocab.pkl'
    p = load_pickle(f)
    return p

def encoder():
    f = 'labelencoder.pkl'
    p = load_pickle(f)
    return p





