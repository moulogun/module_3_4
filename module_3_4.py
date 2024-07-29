def single_root_words(root_word, *other_words):
    same_words = []
    rw = root_word.lower()
    for i in range(0, len(other_words)):
        word = other_words[i].lower()
        count = word.count(rw)
        count2 = rw.count(word)
        if count > 0 or count2 > 0:
            same_words.append(other_words[i])
        else:
            continue
    return(same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)