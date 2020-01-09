"""Initialize Models Here"""
from .model_assets.pre_trained import vocab, rfc, encoder



def load_mvp():

    corpus = vocab()
    forest = rfc()
    le = encoder()

    return corpus, forest, le