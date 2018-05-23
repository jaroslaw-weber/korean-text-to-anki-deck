from googletrans import Translator

translator = Translator()

import csv
#####
# author: Jaroslaw Weber
# email: jaroslaw.weber@gmail.com
# license: MIT
#####

####
# How to use?
# Create two files - input.txt and ignore.txt
# in "input.txt" paste the article you want to analyse
# in "ignore.txt" type what words do you want to ignore (can be empty).
# you can paste here words you already know or don't want to learn.
# run this script with python
####

####
# Example output:
# korean,english,japanese,frequency
# 수가,Number,数,6
# 위해,for,ため,4
# 거짓,lie,偽,4
# 지우다,erase,抹消,4
# ...
####

#output path. dont need to create this file, will be created automatically
word_frequency_file_path = "frequency_list.csv"
output_file_path = "output.csv"
newline = "\n"
separator = ","

print("loading frequency list")

words_with_frequency = {}
words_without_frequency = []

row_index = 0

with open(word_frequency_file_path, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if (row_index > 200):
            print(
                "you can only translate 200 words at once. translating first 200 words"
            )
            break
        word_now = row[0]
        words_with_frequency[word_now] = int(row[1])
        words_without_frequency.append(word_now)
        row_index += 1

print(words_with_frequency)

print("translating")

translations = translator.translate(words_without_frequency, dest='en')
translations_japanese = translator.translate(
    words_without_frequency, dest='ja')

print("creating csv file") 

with open(output_file_path, 'w') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=separator, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    first_row = ["korean", "english", "japanese", "frequency"]
    writer.writerow(first_row)

    for index, translation in enumerate(translations):
        word_now = translation.origin
        frequency_now = words_with_frequency[word_now]
        japanese = translations_japanese[index].text
        row = [word_now, translation.text, japanese, str(frequency_now)]
        writer.writerow(row)

print("created csv file! you can edit it and import it to anki")