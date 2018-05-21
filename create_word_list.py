from konlpy.tag import Kkma
from konlpy.utils import pprint
from googletrans import Translator
translator = Translator()
kkma = Kkma()

#csv file separator
separator = ","
input_file_path = "input.txt"
newline = "\n"

#read input file
with open(input_file_path, 'r') as myfile:
    input_content=myfile.read()

#get nouns
nouns = kkma.nouns(input_content)

#translate and create csv file content
csv_file = ""
translations = translator.translate(nouns, dest='en')
for translation in translations:
    csv_file+= translation.origin+separator+translation.text+newline

#save translations as csv file
with open('output.csv', 'w') as file:
    file.write(csv_file)

print("created csv file!")