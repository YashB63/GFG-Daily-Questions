def maximumFrequency (s) : 
    
    words = s.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    max_count = max(word_counts.values())
    for word in words:
        if word_counts[word] == max_count:
            return word + " " + str(max_count)