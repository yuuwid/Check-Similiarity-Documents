import string
from similiarity.open_file import read_file

   
def get_words_from_line_list(text): 
    str_pattern_1 = string.punctuation + string.ascii_uppercase
    str_pattern_2 = " " * len(string.punctuation) + string.ascii_lowercase
    translation_table = str.maketrans(str_pattern_1, str_pattern_2)

    text = text.translate(translation_table)
    word_list = text.split()
    return word_list


def count_frequency(word_list): 
    D = {}
    
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1

    return D
  
  
def word_frequencies_for_file(filename): 
    char_list = read_file(filename)
    word_list = get_words_from_line_list(char_list)
    freq_mapping = count_frequency(word_list)

    # print("File", filename, ":", )
    # print(len(char_list), "lines, ", )
    # print(len(word_list), "words, ", )
    # print(len(freq_mapping), "distinct words")
    # print()

    return len(word_list), len(char_list), freq_mapping