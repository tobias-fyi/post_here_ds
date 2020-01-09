"""Initialize Models Here"""
from .model_assets.pre_trained import vocab, multiNB, encoder



def load_mvp():

    corpus = vocab()
    nb = multiNB()
    le = encoder()

    return corpus, nb, le