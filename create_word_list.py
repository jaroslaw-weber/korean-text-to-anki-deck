#from konlpy.tag import Kkma
#from konlpy.utils import pprint
from googletrans import Translator
from konlpy.tag import Twitter
twitter = Twitter()
translator = Translator()
#kkma = Kkma()

#csv file separator
separator = ","
input_file_path = "input.txt"
newline = "\n"

#read input file
with open(input_file_path, 'r') as myfile:
    input_content=myfile.read()
    input_content = input_content.decode('string-escape').decode("utf-8")

#print("content:"+input_content)

#get nouns
#nouns = kkma.nouns(input_content)
#print("found nouns")
#nouns = []
#get nouns, adjectives and verbs
print("analysing text")
all_words = twitter.pos(input_content, norm=True, stem=True)

filtered_words = []
for word, word_type in all_words:
    filtered_words.append(word)
    #print("type" + word_type)
    #if(word_type== "typeNoun" or word_type =="typeVerb"):
     #   print(word)


print("translating")
#translate and create csv file content
csv_file = ""
translations = translator.translate(filtered_words, dest='en')
for translation in translations:
    csv_file+= translation.origin+separator+translation.text+newline

#save translations as csv file
with open('output.csv', 'w') as file:
    file.write(csv_file.encode("utf-8"))

print("created csv file!")
