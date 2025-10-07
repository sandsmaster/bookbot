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


def sort_char(char_stats):
    char_dicts = []
    for char in char_stats:
        if char.isalpha():
            char_dicts.append({"char": char, "num": char_stats[char]})
    char_dicts.sort(key=lambda x: x["num"], reverse=True)
    return char_dicts

def report_stats(wc_num, char_stats):
    print(f'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {wc_num} total words''')
    print("--------- Character Count -------")
    for stat in char_stats:
        print(f"{stat['char']}: {stat['num']}")
    print("============= END ===============")
    return 0
    
