# What?

Generating word lists from articles (korean, export to Anki), sort them by frequency and add translation.

# Details

Example output:

```csv
korean,english,japanese,frequency
그거,that,それ,9
둘,couple,両方,9
올해,this year,今年,9
그때,then,その,9
```

As you can see, it creates list from most frequent (useful) words. You can put whole book (or novel) and analyse it.

You can filter words so the list does not contain words you already know.

You can find novels here:

http://novel.naver.com/webnovel/weekday.nhn

Creating frequency list from novels is very useful. You can memorize most frequent word in the novel you want to read, and understand more.
Then, you can solidify this knowledge by reading the novel! You can mix up SRS (memorizing words with Anki) with reading practice.

# What is Anki?

https://apps.ankiweb.net/

It is great tool for memorizing words (and anything else).

# How to import frequency list to Anki?

Try search it with google:

[https://www.google.com/search?q=anki+csv+import](https://www.google.com/search?q=anki+csv+import)

# What is the quality of the translation?

There are lot of errors in translation (especially in Japanese), so better fix the translation with [Naver Dictionary](http://endic.naver.com/?sLn=en)!

Useful Anki plugins:
- [Hanseido](https://ankiweb.net/shared/info/367700876)
- [Japanese Definitions for Korean Vocabulary](https://ankiweb.net/shared/info/553926167)

# Installation

- install python
[https://www.python.org/downloads/](https://www.python.org/downloads/)
- install konply (korean text analysis tool)
[http://konlpy.org/en/v0.4.4/install/](http://konlpy.org/en/v0.4.4/install/)
- install googletrans
[https://pypi.org/project/googletrans/](https://pypi.org/project/googletrans/)

# How to use

- create input.txt file with text to analyse

- define words to ignore in ignore.txt file (one word per line)

- edit "create_frequency_list" file and change "filter_below_frequency" settings to desired value (try with 2-3 for short texts, 5-8 for longer texts)

- type this to create frequency list
```
python create_frequency_list.py
```
- type this to translate frequency list (only translating top 200 words from frequency list)
```
python translate_frequency_list.py 
```

# FAQ

> How the tool is handling verbs? Verbs are often conjugated

The tool is detecting that verb is conjugated and transforms it to "base form".
