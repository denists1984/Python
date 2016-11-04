def word_count(word):
    new_dict = {}
    list_dict = word.lower().split(" ")
    for a in list_dict:
        if a in list_dict[a]:
            new_dict[a] += 1
        else:
            new_dict[a] = 1

    return new_dict
