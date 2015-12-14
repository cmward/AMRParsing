import sys
import numpy as np
from gensim.models import Word2Vec

""" Script to write vectors from a gensim Word2Vec model to plain text.

Usage:
    python write_vecs.py /path/to/model /path/to/output

"""

def write_model(model, fname):
    """ Write word vectors to `fname`
    """
    with open(fname, 'w+') as outfile:
        for i,w in enumerate(model.index2word):
            try:
                outfile.write("{} {}\n".format(
                    w.encode('utf-8'),
                    ' '.join([str(n) for n in model.syn0[i]])))
            except UnicodeDecodeError:
                outfile.write("{} {}\n".format(
                    w, ' '.join([str(n) for n in model.syn0[i]])))
        print "Wrote vectors to {}".format(fname)
            
def main(model_name, fname):
    print "Loading model..."
    model = Word2Vec.load(model_name)
    print "Writing vectors from {} to {}...".format(model_name, fname)
    write_model(model, fname)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

