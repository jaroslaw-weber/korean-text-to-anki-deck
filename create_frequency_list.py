from konlpy.tag import Twitter

twitter = Twitter()

#csv file separator
separator = ","
#path to article/text in korean!
input_file_path = "input.txt"
#path to words to ignore. words should be separated with new line! so, file with one word per line
ignore_file_path = "ignore.txt"

output_file_path = "frequency_list.csv"

#more messages!!! set to True if something is broken
debug_mode = False

#filtering words that are not frequent. for example, setting this to 1 would filter all words that appeared less than once.
#for short texts set to 1, for very long texts set to higher value (10 or more)
filter_below_frequency = 7

import collections
import csv

#read input file
if debug_mode:
    print("reading input.txt file")
with open(input_file_path, 'r') as myfile:
    input_content = myfile.read()
    input_content = input_content  #.decode('string-escape').decode("utf-8")

#get nouns, adjectives and verbs
if debug_mode:
    print("analysing text")
all_words = twitter.pos(input_content, norm=True, stem=True)

if debug_mode:
    print("filtering words")
filtered_words = []
for word, word_type in all_words:
    #filter only important words
    if (word_type == "Noun" or word_type == "Verb" or word_type == "Adjectives"):
        #print(word)
        filtered_words.append(word)

if debug_mode:
    print("counting words")
words_counter = collections.Counter(filtered_words)

total_words_count = sum(words_counter.values())

print("total words count: "+ str(len(all_words)))
print("unique words count: " + str(total_words_count))

if debug_mode:
    print("loading ignore file: " + ignore_file_path)
with open(ignore_file_path, 'r') as myfile:
    #words to remove form list
    words_to_ignore = set(myfile.read().splitlines())
    

if debug_mode:
    print("removing ignored words")
for key, cnts in list(words_counter.items()):
    if (key in words_to_ignore):
        del words_counter[key]

if debug_mode:
    print("removing not frequent words")

#recalculating total words count after removing ignored words
total_words_count = sum(words_counter.values())
deleted_words_count = 0

#removing words with low frequency
for key, cnts in list(words_counter.items()):
    if cnts < filter_below_frequency:
        del words_counter[key]
        deleted_words_count += cnts

percent = (total_words_count - deleted_words_count) / total_words_count * 100
percent = int(round(percent))

frequency_list_length = len(words_counter.values())
print("words to learn: " + str(frequency_list_length))
percent_text = "understand {}% of the text!".format(
    percent)
print(percent_text)

#getting most common words
words_with_frequency = words_counter.most_common()
words_without_frequency = [i[0] for i in words_with_frequency]

with open(output_file_path, 'w') as csvfile:
    spamwriter = csv.writer(
        csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for word in words_without_frequency:
        frequency_now = words_counter[word]
        row = [word, str(frequency_now)]
        spamwriter.writerow(row)
