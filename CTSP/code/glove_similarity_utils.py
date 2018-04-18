import numpy as np
import os


def load_embeddings(filename):
	'''
	Function source: Berkeley CS 194-129, Homework 3.
	'''
    vocab = []
    embed = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            row = line.strip().split(' ')
            vocab.append(row[0])
            embed.append(row[1:])
    embed = np.asarray(embed).astype(np.float32)
    return vocab, embed

def load_glove():
	'''
	Function source: Berkeley CS 194-129, Homework 3.
	'''
	# Load the GloVe vectors into numpy
	glove_filepath = os.path.join('datasets', 'glove.6B.50d.txt')
	vocab, embed = load_embeddings(glove_filepath)
	vocab_size = len(vocab)
	embed_dim = len(embed[0])
	assert vocab_size > 0, "The vocabulary shouldn't be empty; did you download the GloVe weights?"
	print('Loaded %d %d-dimensional embeddings.' % (vocab_size, embed_dim))

def get_embed_for_words(words, vocab):
    word_embeds = []
    fin_words = []
    for i in range(400000):
        for word in words:
            if word == vocab[i]: 
                print('Word {} is in the dataset'.format(vocab[i]))
                fin_words.append(word)
                word_embeds.append(embed[i])
                words.remove(vocab[i])
    return fin_words, word_embeds

def compute_sim_matrix(normalized_category_embeds, normalized_tag_embeds): 
	# convert dtype to float from string.
	category_embeds = category_embeds.astype(np.float32)
	tag_embed_matrix = tag_embed_matrix.astype(np.float32)

	# normalize your embeddings by l2 norm. saves an extra step later
	normalized_tag_embeds = tag_embed_matrix * (1 / np.linalg.norm(tag_embed_matrix, axis=0))
	normalized_category_embeds = category_embeds * np.expand_dims(1 / np.linalg.norm(category_embeds, axis=1), -1)

	#Compute matmul and masking.
	sim_matrix = np.matmul(normalized_category_embeds, normalized_tag_embeds)
	masked_sim_matrix = sim_matrix * (sim_matrix >= 0)
	return masked_sim_matrix

def compute_total_score(sim_matrix): 
	num_entries = sim_matrix.shape[0] * sim_matrix.shape[1]
	return np.sum(sim_matrix) / num_entries