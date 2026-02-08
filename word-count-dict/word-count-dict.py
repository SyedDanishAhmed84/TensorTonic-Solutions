def word_count_dict(sentences):
    frequency={}
    for sentence in sentences:
        for word in sentence:
            frequency[word]=frequency.get(word,0)+1

    return frequency        


