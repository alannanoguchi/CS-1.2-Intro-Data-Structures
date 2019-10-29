import os
os.system("python source_text.txt")


def histogram_dictionary(source_text):
    """Reads source_text and returns a dictionary (as a histogram) of the words"""
    histogram = {}
    for word in source_text:
        word = word.lower()
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram


def histogram_lists(source_text):
    histogram = []
    added_word = True

    for word in source_text:
        for item in histogram:
            if item[0] == word:
                item[1] += 1
                added_word = False
        if added_word is True:
            histogram.append([word,1])
        added_word = True

    return histogram





if __name__ == '__main__':
    text = "source_text.txt"