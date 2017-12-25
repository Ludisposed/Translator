from collections import Counter
import numpy as np
def read_sentences(filename):
	sentences = []
	with open(filename, 'r') as f:
		for line in f:
			sentences.append(line.replace('\r\n',''))
	return sentences
def create_dataset(en_sentences, fr_sentences):
	en_vocab_dict = Counter(word.strip(',." ;:)(][?!') for sentence in en_sentences for word in sentence.split())
	fr_vocab_dict = Counter(word.strip(',." ;:)(][?!') for sentence in fr_sentences for word in sentence.split())

	en_vocab = list(map(lambda x: x[0], sorted(en_vocab_dict.items(), key = lambda x: -x[1])))
	fr_vocab = list(map(lambda x: x[0], sorted(fr_vocab_dict.items(), key = lambda x: -x[1])))
	
	en_vocab = en_vocab[:20000]
	fr_vocab = fr_vocab[:30000]

	start_idx = 2
	en_word2idx = dict([(word, idx+start_idx) for idx, word in enumerate(en_vocab)])
	en_word2idx['<ukn>'] = 0
	en_word2idx['<pad>'] = 1
	en_idx2word = dict([(idx, word) for word, idx in en_word2idx.items()])

	start_idx = 4
	fr_word2idx = dict([(word, idx+start_idx) for idx, word in enumerate(fr_vocab)])
	fr_word2idx['<ukn>'] = 0
	fr_word2idx['<go>']  = 1
	fr_word2idx['<eos>'] = 2
	fr_word2idx['<pad>'] = 3
	fr_idx2word = dict([(idx, word) for word, idx in fr_word2idx.items()])

	x = [[en_word2idx.get(word.strip(',." ;:)(][?!'), 0) for word in sentence.split()] for sentence in en_sentences]
	y = [[fr_word2idx.get(word.strip(',." ;:)(][?!'), 0) for word in sentence.split()] for sentence in fr_sentences]

	X = []
	Y = []

	en_max_len = 0
	fr_max_len = 0

	for i in range(len(x)):
		n1 = len(x[i])
		n2 = len(y[i])

		if abs(n1 - n2) <= 4 and max(n1,n2) <= 15:
			en_max_len = en_max_len if n1 <= en_max_len else n1
			fr_max_len = fr_max_len if n2 <= fr_max_len else n2
			X.append(x[i])
			Y.append(y[i])
	return X, Y, en_word2idx, en_idx2word, en_vocab, en_max_len, fr_word2idx, fr_idx2word, fr_vocab, fr_max_len

def batch(inputs):
	sequence_lengths = [len(seq) for seq in inputs]
	batch_size = len(inputs)

	max_sequence_length = max(sequence_lengths)
	inputs_batch_major = np.zeros(shape=[batch_size, max_sequence_length], dtype=np.int32) # == PAD

	for i, seq in enumerate(inputs):
		for j, element in enumerate(seq):
			inputs_batch_major[i, j] = element

	inputs_time_major = inputs_batch_major.swapaxes(0, 1)
	return inputs_time_major, sequence_lengths

