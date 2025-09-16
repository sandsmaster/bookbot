def wc(text):
    return len(text.split())

def char_stats(text):
    stats_dict = {}
    for c in text:
        c = c.lower()
        if c in stats_dict:
            stats_dict[c] += 1
        else:
            stats_dict[c] = 1
    
    return stats_dict
