def remove_stopwords(tokens, stopwords):
    stopwords_set=set(stopwords)
    
    filtered_tokens=[token for token in tokens if token not in stopwords]
    
    return filtered_tokens