#twitterのツイートを抽出し、mecabで文字を分けて
import MeCab
import numpy as np
from collections import Counter
import re

count_noun = Counter()
tagger = MeCab.Tagger()
select = False
select_type = False
select_part = False

def extract_by_parse(sentence,word_p,word_n):
  nouns = []
  parsed=tagger.parse(sentence)
  for chunk in parsed.splitlines()[:-1]:
    (surface, feature) = chunk.split('\t')
    if (feature.split(',')[word_n]==word_p):
      nouns.append(surface)
  return nouns

print("ツイート品詞登場ランキングを表示します")
while select==False:
  print("選んでください 1:メインアカウント 2:趣味アカウント 3:サブアカウント 4:いにしえのアカウント")
  select_f = input()
  if select_f == "1":
    data = "data/mainAccount/"
    select = True
  elif select_f == "2":
    data = "data/splatoonAccount/"
    select = True
  elif select_f == "3":
    data = "data/subAccount/"
    select = True
  elif select_f == "4":
    data = "data/oldAccount/"
    select = True

while select_type == False:
  print("ツイートorライク 1:Tweet 2:Like")
  select_t = input()
  if select_t == "1":
    data += "tweet.js"
    select_type = True
  elif select_t == "2":
    data += "like.js"
    select_type = True

# print(data)

print("どの品詞を抽出しますか？")
while select_part == False:
  print("選んでください 1:固有名詞 2:名詞 3:形容詞 4:動詞 5:助詞 6:助動詞 7:副詞")
  select_p = input()
  if select_p == "1":
    word_p = "固有名詞"
    word_n = 1
    select_part = True
  elif select_p == "2":
    word_p = "名詞"
    word_n = 0
    select_part = True
  elif select_p == "3":
    word_p = "形容詞"
    word_n = 0
    select_part = True
  elif select_p == "4":
    word_p = "動詞"
    word_n = 0
    select_part = True
  elif select_p == "5":
    word_p = "助詞"
    word_n = 0
    select_part = True
  elif select_p == "6":
    word_p = "助動詞"
    word_n = 0
    select_part = True
  elif select_p == "7":
    word_p = "副詞"
    word_n = 0
    select_part = True




f=open(data, "r",  encoding ="utf-8")
lines = f.readlines()
for line in lines:
  line = line.replace(' ','')
  p = line.startswith('"full_text')
  q = line.startswith('"fullText')
  if p or q:
    line = line.replace('"full_text":"','').replace('"fullText":"','').replace('n','').replace('"','').replace(',','').replace('\\','')
    line = line[:line.find('https://t.co')]
    if line.startswith('RT@') or line.startswith('@'):
      continue
    noun = extract_by_parse(line,word_p,word_n)
    for word in noun:
      count_noun[word] += 1

c = 0

count_noun = sorted(count_noun.items(), key=lambda x:x[1],reverse=True)

print('------'+ word_p +'result------')
for key in count_noun:
  print(key)
  c+=1
  if c > 10: break