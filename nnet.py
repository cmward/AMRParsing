from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Embedding
from keras.optimizers import SGD, RMSProp

class Net(object):
    def __init__(self, embdim, output_dim, index_dict, weights_file=None):
        n_vocab = len(index_dict)
        weights = np.zeros((n_vocab, embdim))
        for word,index in index_dict.items():
            weights[index,:] = word_vectors[word]

        self.model = Sequential()
        self.model.add(Embedding(input_dim=n_vocab, output_dim=embdim,
                                 input_length=2, weights=[weights]))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(250, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(10, activation='softmax'))

    def batch_fit(self, X_batch, Y_batch, batch_size=128):
        self.model.compile(loss='categorical_crossentropy', optimizer=RMSProp)
        self.model.train_on_batch(X_batch, Y_batch)

    def predict(X_test, batch_size=1):
        classes = self.model.predict_classes(X_test, batch_size=batch_size)
        return classes
