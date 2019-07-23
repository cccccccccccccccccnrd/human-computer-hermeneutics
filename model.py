import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=150000)

def get_nearest(positive=None, negative=None):
    try:
        similar = model.most_similar(positive=positive, negative=negative, topn=5)
        return [entry[0] for entry in similar]
    except:
        return None

def get_vector(word):
    return "{!s}".format(model[word])