import numpy as np

def bag_of_words_vector(tokens, vocab):

    vocab_index = {word: i for i, word in enumerate(vocab)}
    
    bow_vector = np.zeros(len(vocab), dtype=int)
    
    # Count occurrences
    for token in tokens:
        if token in vocab_index:
            bow_vector[vocab_index[token]] += 1
            
    return bow_vector
