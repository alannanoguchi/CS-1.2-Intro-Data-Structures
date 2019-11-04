import os 
import re
# if you are messing with files ouside of the actual app, you have to import os



def histogram_dictionary(source_text):
    """Reads source_text and returns a dictionary (as a histogram) of the words"""
    lines = data.readlines()
    # print(lines)
    # histogram = {}
    for line in lines:
        # remove_chars = line.rstrip(["!?,.;:"])
        # words = line.split(" ")
        line = re.sub(r"[^a-z0-9]"," ",line.lower())
        words = line.split(' ')
        for word in words:
            
            if word in histogram:
                histogram[word] = histogram.get(word, 0) + 1
            else:
                histogram[word] = 1
    return histogram
        
        

def unique_words(dict):
    # return len(dict)
    print(len(dict))


def frequency(word, dict):
    # TODO: print the value of the key
    for value in histogram:
        # return histogram[value]
        print (value, histogram[value])




if __name__ == '__main__':
    histogram = {}
    with open("sample.txt", "r") as data:
        histogram_dictionary(data)
        unique_words(histogram)
        frequency("is", histogram)
   