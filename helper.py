import numpy as np

data = open('input.txt').read()
chars = list(set(data))
data_size, vocab_size = len(data), len(chars)
char_to_ix = {ch:i for i, ch in enumerate(chars)}
ix_to_char = {i:ch for i, ch in enumerate(chars)}

def batch(inputs, max_sequence_length=None):
    """
    Args:
        inputs:
            list of sentences (integer lists)
        max_sequence_length:
            integer specifying how large should `max_time` dimension be.
            If None, maximum sequence length would be used
    
    Outputs:
        inputs_time_major:
            input sentences transformed into time-major matrix 
            (shape [max_time, batch_size]) padded with 0s
        sequence_lengths:
            batch-sized list of integers specifying amount of active 
            time steps in each input sequence
    """
    
    sequence_lengths = [len(seq) for seq in inputs]
    batch_size = len(inputs)
    
    if max_sequence_length is None:
        max_sequence_length = max(sequence_lengths)
    
    inputs_batch_major = np.zeros(shape=[batch_size, max_sequence_length], dtype=np.int32) # == PAD
    
    for i, seq in enumerate(inputs):
        for j, element in enumerate(seq):
            inputs_batch_major[i, j] = element

    # [batch_size, max_time] -> [max_time, batch_size]
    inputs_time_major = inputs_batch_major.swapaxes(0, 1)

    return inputs_time_major, sequence_lengths


def random_sequences(length_from, length_to,
                     vocab_lower, vocab_upper,
                     batch_size):
    """ Generates batches of random integer sequences,
        sequence length in [length_from, length_to],
        vocabulary in [vocab_lower, vocab_upper]
    """
    if length_from > length_to:
            raise ValueError('length_from > length_to')

    def random_length():
        if length_from == length_to:
            return length_from
        return np.random.randint(length_from, length_to + 1)
    
    while True:
        yield [
            np.random.randint(low=vocab_lower,
                              high=vocab_upper,
                              size=random_length()).tolist()
            for _ in range(batch_size)
        ]
p = 0
def generate_sequence(length, batch_size):

    global p
    sequence = []
    for _ in range(0,batch_size):
        if p + length + 1 >= len(data):
            p = 0
        sequence.append([char_to_ix[ch] for ch in data[p:p+length]])
        p += length
    while True:
        yield sequence

def decode(sequence):
    s = ""
    for i in sequence:
        s += ix_to_char[i]
    return s
def encode(charecters):
    s = []
    for c in charecters:
        s.append(char_to_ix[c])
    return s





#en-fr


def data_info(filename):
    sentences = []
    data = ""
    with open(filename, 'r') as f:
        for line in f:
            sentences.append(line)
            data += line.replace('\n',' ')
    words = data.split(' ')
    vocab_size = len(words)
    char_to_ix = {ch:i for i, ch in enumerate(words)}
    ix_to_char = {i:ch for i, ch in enumerate(words)}


    n = int(len(sentences) * 0.9)
    train_sentences = sentences[:n]
    test_sentences = sentences[n:]

    return train_sentences, test_sentences, vocab_size, char_to_ix, ix_to_char

def sentence_sequence(sentence, c2x):
    words = sentence.split(' ')[:-1]
    sequence = []
    for w in words:
        sequence.append(c2x[w])
    return sequence

def generate_trans_sequence(sentences, c2x):

    sequence = []
    for sentence in sentences:
        sequence.append(sentence_sequence(sentence, c2x))
    while True:
        yield sequence

def decode_trans(language, sequence, x2c):
    words = []
    for s in sequence:
        words.append(x2c[s])
    return ' '.join(words)