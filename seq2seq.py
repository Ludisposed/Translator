from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers import Input, Activation, Dense, Permute, Dropout, add, dot, concatenate
from keras.layers import LSTM
from keras.preprocessing.sequence import pad_sequences
from keras.layers.wrappers import Bidirectional
import helper
import numpy as np
en_sentences = helper.read_sentences('data/small_vocab_en')
fr_sentences = helper.read_sentences('data/small_vocab_fr')

X, Y, en_word2idx, en_idx2word, en_vocab, en_max_len, fr_word2idx, fr_idx2word, fr_vocab, fr_max_len = helper.create_dataset(en_sentences, fr_sentences)

encoder_hidden_units = 20
decoder_hidden_units = encoder_hidden_units * 2

en_vocab_size = len(en_vocab)
fr_vocab_size = len(fr_vocab)

hidden_size = 216
sentence_num = len(X)
s = int(sentence_num // 0.9)

en_train = X[:s]
fr_train = Y[:s]

en_test = X[s:]
fr_test = Y[s:]

en_train = pad_sequences(en_train, maxlen=en_max_len, padding='post', truncating='post')
fr_train = pad_sequences(fr_train, maxlen=fr_max_len, padding='post', truncating='post')

en_test = pad_sequences(en_test, maxlen=en_max_len, padding='post', truncating='post')
fr_test = pad_sequences(fr_test, maxlen=fr_max_len, padding='post', truncating='post')

#input layer
en_input = Input((en_max_len,))
fr_target = Input((fr_max_len,))

#encode
#embedding
en_emb = Embedding(input_dim = en_vocab_size, output_dim = hidden_size, input_length = en_max_len)(en_input)
#lstm
en_lstm = LSTM(encoder_hidden_units)(en_emb)
#bidirectional
en_bid = Bidirectional(en_lstm)

#decode
#embedding
fr_emb = Embedding(input_dim = fr_vocab_size, output_dim = hidden_size, input_length = fr_max_len)(fr_target)
#lstm
fr_lstm = LSTM(decoder_hidden_units)(fr_emb)


