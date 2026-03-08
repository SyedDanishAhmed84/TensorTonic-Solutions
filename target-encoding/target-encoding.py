def target_encoding(categories, targets):
    sums = {}
    counts = {}
    
    for c, t in zip(categories, targets):
        sums[c] = sums.get(c, 0) + t
        counts[c] = counts.get(c, 0) + 1
    
    means = {}
    for c in sums:
        means[c] = sums[c] / counts[c]
    
    result = []
    for c in categories:
        result.append(float(means[c]))
    
    return result