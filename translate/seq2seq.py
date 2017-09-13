import numpy as np
import tensorflow as tf
from tensorflow.python.ops.rnn_cell import LSTMCell, LSTMStateTuple
import helper
class Seq2SeqModel(object):
	def __init__(self,
		         vocab_size,
		         input_embedding_size):
		self.encoder_inputs = tf.placeholder(shape = (None, None), dtype = tf.int32, name = 'encoder_inputs')
		self.encoder_inputs_length = tf.placeholder(shape = (None,), dtype = tf.int32, name = 'encoder_inputs_length')
		self.decoder_targets = tf.placeholder(shape=(None, None), dtype = tf.int32, name = 'decoder_targets')
		self.embeddings = tf.Variable(tf.random_uniform([vocab_size, input_embedding_size], -1.0, 1.0), dtype = tf.float32)
		self.encoder_inputs_embedded = tf.nn.embedding_lookup(embeddings, self.encoder_inputs)

		tf.reset_default_graph()
		self.sess = tf.InteractiveSession()
	def encode(self, encoder_hidden_units):
		self.encoder_cell = LSTMCell(encoder_hidden_units)
	def train(self):
		

batch_size = 100
batches = helper.random_sequences(length_from=3, length_to=8,
                                   vocab_lower=2, vocab_upper=10,
                                   batch_size=batch_size)
def next_feed():
    batch = next(batches)
    encoder_inputs_, encoder_input_lengths_ = helper.batch(batch)
    decoder_targets_, _ = helper.batch(
        [(sequence) + [EOS] + [PAD] * 2 for sequence in batch]
    )
    return {
        encoder_inputs: encoder_inputs_,
        encoder_inputs_length: encoder_input_lengths_,
        decoder_targets: decoder_targets_
    }

loss_track = []

max_batches = 3001
batches_in_epoch = 1000

try:
    for batch in range(max_batches):
        fd = next_feed()
        _, l = sess.run([train_op, loss], fd)
        loss_track.append(l)

        if batch == 0 or batch % batches_in_epoch == 0:
            print('batch {}'.format(batch))
            print('  minibatch loss: {}'.format(sess.run(loss, fd)))
            predict_ = sess.run(decoder_prediction, fd)
            for i, (inp, pred) in enumerate(zip(fd[encoder_inputs].T, predict_.T)):
                print('  sample {}:'.format(i + 1))
                print('    input     > {}'.format(inp))
                print('    predicted > {}'.format(pred))
                if i >= 2:
                    break
            print()

except KeyboardInterrupt:
    print('training interrupted')


